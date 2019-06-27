import requests
import bleach
import json
import csv

f = open('output.json', 'w')

urls = []
with open('king_list.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:
        tmp = {"url":row[0], "pos":[row[1], row[2]]}
        urls.append(tmp)

list = []
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
    list.append(tmp)

json.dump(list, f)
f.close()
#print(bleach.clean(data['html']))
