#just a memo
#killed pythonされたファイル
#なぜkillされたのかわからないのでとりあえずメモ

#koneko_navy.exe
>>> import pefile
>>> pe = pefile.PE('/tmp/vector/koneko_navy.exe')
>>> pe.parse_data_directories()
zsh: killed     python
  
  
#zipextractor.exe
$ python auto.py non-malicious-file/zipextractor.exe                                                         []
zsh: killed     python auto.py non-malicious-file/zipextractor.exe
