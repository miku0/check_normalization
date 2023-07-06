import MeCab
#wakati = MeCab.Tagger("-Owakati")
#print(wakati.parse("西新宿二丁目").split())
#import MeCab

# MeCabのインスタンスを作成
#m = MeCab.Tagger('-Ochasen -u /home/miku/mecab/addr.dic')
#m = MeCab.Tagger()
#m = MeCab.Tagger('-d /usr/share/mecab/dic/ipadic -u ./addr.dic')
#m = MeCab.Tagger('d /var/lib/mecab/dic/debian/sys.dic -u /home/miku/mecab/addr.dic')
m = MeCab.Tagger('-d /var/lib/mecab/dic/debian -u /home/miku/mecab/addr.dic')
# テキストを形態素解析
text = "東京都港区芝公園4-2-8"
result = m.parse(text)
text = "北海道札幌市中央区4-2-8"
result = m.parse(text)


# 結果を表示
print(result)
