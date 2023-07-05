import csv
import chardet

csv_path = "KEN_ALL.CSV"

# ファイルのエンコーディングを検出
with open(csv_path, 'rb') as file:
    result = chardet.detect(file.read())
encoding = result['encoding']

# エンコーディングを使用してCSVファイルを読み込む
with open(csv_path, encoding=encoding) as csv_file:
    csv_reader = csv.reader(csv_file)
    for _ in range(2):  # 上から2行を表示する
        row = next(csv_reader, None)
        if row is not None:
            print(row)

