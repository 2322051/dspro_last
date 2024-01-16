import csv
import sqlite3

# SQLiteデータベースに接続
conn = sqlite3.connect('tenki.sqlite')
cursor = conn.cursor()

# テーブルの作成local
cursor.execute('''
    CREATE TABLE IF NOT EXISTS local_tenki (
        date TEXT PRIMARY KEY,
        steps TEXT,
        stride_median TEXT,
        calories_burned TEXT,
        sedentary_calories_burned TEXT
    )
''')



# SQLiteデータベースに接続
conn = sqlite3.connect('tenki.sqlite')
cursor = conn.cursor()

# CSVファイルの読み込みとデータベースへの挿入
with open('/Users/takuto/dspro_last/ds_tenki/dspro_ローカルデータ.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # ヘッダー行がある場合、読み飛ばす
    next(csv_reader)

    for row in csv_reader:
        cursor.execute('''
            INSERT INTO local_tenki (date, steps, stride_median, calories_burned, sedentary_calories_burned)
            VALUES (?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4]))

# コミットとクローズ
conn.commit()
conn.close()