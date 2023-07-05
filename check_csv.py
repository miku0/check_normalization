import csv
import re
import sys

sample_address = "東京都文京区後楽１丁目３−６１"
sample_answer = ["東京都", "文京区", "後楽１丁目３−６１"]

extreme_address = "壱丁目二番地３号都道府県市区町村ハイツ456号室"

# 住所データを取得 (同じフォルダ内のKEN_ALL.csvを読み込む)
print("\nKEN_ALL.csvをパース中... ", end="")
address_list = []
csv_path = "./KEN_ALL.CSV"
try:
    with open(csv_path, encoding="Shift_JIS") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 9:
                if extreme_address:
                    address_list.append([*row[6:8], f"{row[8]}{extreme_address}"])
                else:
                    address_list.append(row[6:9])
except FileNotFoundError:
    print("\n\nERROR: KEN_ALL.CSVが存在しません。")
    print("  以下のzip内のKEN_ALL.CSVをこのスクリプトと同じフォルダに置いてください。")
    print("  http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip\n\n")
    sys.exit()
print("完了")

# 無限ループ
while True:
    # 正規表現を取得
    print("\n正規表現を入力してください (control + cで終了)：")
    try:
        rex = re.compile(input().strip())
    except re.error:
        print("\nERROR: 正規表現の作成に失敗しました。")
        print("  ", sys.exc_info()[1])
        continue
    if rex.pattern == "":
        print("ERROR: 文字列が空です。")
        continue

    # サンプル住所で試してみる。駄目だったら入力しなおし。
    m = rex.search(sample_address)
    if m is None or m.groups() != tuple(sample_answer):
        print("\nERROR: サンプル住所の分割に失敗しました。やり直してください。")
        print("  住所:", sample_address)
        print("  正解:", sample_answer)
        print("  回答:", m.groups() if m else [])
        continue

    # 正規表現のマッチ結果を取得
    result = []
    for address in address_list:
        match = rex.search("".join(address))

        if match:
            result.append(list(match.groups()))
        else:
            result.append([])

    # 判定
    fail_count = 0
    for address, match in zip(address_list, result):
        if address != match:
            print(f"失敗... {'|'.join(address)}\t({'|'.join(match)})")
            fail_count += 1

    # 結果を出力
    all_count = len(address_list)
    fail_percent = (fail_count / all_count) * 100
    print("\n正規表現: ", rex.pattern)
    print("\n失敗数: ", f"{fail_count} / {all_count} ({int(fail_percent)}%)")
