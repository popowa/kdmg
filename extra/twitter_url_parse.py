import requests
import bleach
import json
import csv

f = open('output_20190806.json', 'r+')
jsonData = json.load(f)

urls = []
with open('king_list20190806.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    for row in reader:
        y_tmp =  850 - int(row[3])
        url_parse = row[1].split("/")
        tmp = {"url":url_parse[5], "pos":[row[2], str(y_tmp)]}
        urls.append(tmp)

json.dump(urls, f)
f.close()
