import MeCab
wakati = MeCab.Tagger("-Owakati")
print(wakati.parse("西新宿二丁目").split())
