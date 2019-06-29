import requests
import bleach
import json
import csv

'''
https://github.com/popowa/kdmg/issues/1
JSONファイルに追記するのを後で調べる
'''

f = open('output.json', 'r+')
jsonData = json.load(f)

urls = []
with open('king_list_20190626.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    for row in reader:
        y_tmp =  850 - int(row[3])
        tmp = {"url":row[1], "pos":[row[2], y_tmp]}
        urls.append(tmp)

for i in range(len(urls)):
    params = {'url':urls[i]['url']}
    response = requests.get('https://publish.twitter.com/oembed', params=params)
    data = response.json()
    tmp = {
        "url": data['url'],
        "author_name": data['author_name'],
        "author_url":data['author_url'],
        "html":data['html'],
        "pos": urls[i]["pos"]
    }
    jsonData.append(tmp)

json.dump(jsonData, f)
f.close()
