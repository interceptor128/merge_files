import os
import sys
from tqdm import tqdm

args = sys.argv

def merge_files(defpath, deffilename):
    # 入力（ディレクトリ指定）
    path = defpath

    # 初期化
    files = []

    # ディレクトリ内のフォルダファイル一覧を取得
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):    # ファイルのみ取得
            files.append(path + '\\' + filename)

    # 出力（ファイル名指定）
    outfilepath = path + '\\' + deffilename

    # ファイルマージ
    with open(outfilepath, 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                for line in tqdm(infile):
                    outfile.write(line)

# メイン処理
if __name__ == '__main__':
    args = sys.argv
    if 3 == len(args):
        merge_files(args[1],args[2])
    else:
        print('Arguments are too short')