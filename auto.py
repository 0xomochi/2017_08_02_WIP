#coding: UTF-8
#pythonでvagrant上のファイルを自動で
#読み込み
#pefileで特徴抽出（APIリスト）
#pickleに書き込み, 保存
#"python auto.py path/to/file"で実行

##ファイルの読み込み
import sys

argvs = sys.argv
argc = len(argvs)

#pefileで特徴抽出
import pefile

api_data = []
pe = pefile.PE(argvs[1])
pe.parse_data_directories()
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    for imp in entry.imports:
        api_data.append(imp.name)

#pickleに保存
import pickle

with open("apilist.pickle", "rb") as x:
    data = pickle.load(x)

data.append(api_data)

with open("apilist.pickle", "wb") as x:
    pickle.dump(data, x)
