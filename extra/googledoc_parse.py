import requests
import bleach
import json
import csv

#f = open('cp_20191016.json', 'r+')
#jsonData = json.load(f)

#urls = []
with open('cp_20191016.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    num = 0
    for row in reader:
        print("[", "\"%s\"," % row[1], "\"p%s\"," % num, "\"%s\"" % row[2], "],")
        print("[", "\"%s\"," % row[3], "\"p%s\"," % num, "\"%s\"" % row[4], "],")
        num+=1
