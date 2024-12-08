# ファイルパス (WindowsのDownloadsフォルダ内)
file_path = r"C:\Users\<ユーザー名>\Downloads\py\uBlacklist.txt"

# ファイルを読み込み
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 重複を削除し、アルファベット順に並べ替え
unique_sorted_lines = sorted(set(line.strip() for line in lines))

# 結果を元のファイルに上書き保存
with open(file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(unique_sorted_lines))

print("重複を削除し、アルファベット順に並べ替えました。")
