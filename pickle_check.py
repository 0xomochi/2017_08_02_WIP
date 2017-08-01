#pickleの動作確認
#"apilist.pickle"上に書き込まれたAPIリストの一覧を見る
#APIリストは二次元配列で格納
#python対話モード


import pickle
with open("apilist.pickle", "rb") as f:
	data = pickle.load(f)

#"data"で配列を出力
