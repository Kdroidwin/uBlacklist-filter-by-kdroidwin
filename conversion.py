import re

def process_urls(input_file, output_file):
    # 読み込むファイル
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 結果を格納するリスト
    filtered_lines = []

    # 各行を処理
    for line in lines:
        # 行が削除条件に合致する場合はスキップ
        if any(keyword in line for keyword in ["note.com", "twitter.com", "x.com", "ameblo.jp", "livedoor", "blogger"]):
            continue
        if line.startswith("/"):  # `/` から始まる行をスキップ
            continue
        if line.startswith("title"):  # `title` から始まる行をスキップ
            continue

        # URLを置換
        line = re.sub(r"\*://\*\.000webhostapp\.com/\*", r"||*.000webhostapp.com^", line)  # `000webhostapp.com`
        line = re.sub(r"\*://13377x\.io/\*", r"||13377x.io^", line)  # `13377x.io`
        line = re.sub(r"\*://\*\.ac\.id/\*", r"||*.ac.id^", line)  # `*.ac.id`

        # 結果リストに追加
        filtered_lines.append(line)
    
    # フィルタリング後の内容を保存
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

    # 成功メッセージ
    print("uBlock Origin の形式に変換されました。")

# 入力ファイルと出力ファイルを指定
input_file = 'input.txt'  # 元のデータファイル
output_file = 'output.txt'  # 処理後の保存先

process_urls(input_file, output_file)
