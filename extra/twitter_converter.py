import requests
import bleach
import json
import csv

'''
https://github.com/popowa/kdmg/issues/1
JSONファイルに追記するのを後で調べる
https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed.html
'''

f = open('output_20190806.json', 'r+')
jsonData = json.load(f)
urls = []
with open('king_list_20190806.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    for row in reader:
        y_tmp =  850 - int(row[3])
        tmp = {"url":row[1], "pos":[row[2], str(y_tmp)]}
        urls.append(tmp)

for i in range(len(urls)):
    params = {'url':urls[i]['url']}
    print('Fetch...'+urls[i]['url'])
    response = requests.get('https://publish.twitter.com/oembed', params=params)
    if(response):
        data = response.json()
        print('OK')
        tmp = {
            "url": data['url'],
            "author_name": data['author_name'],
            "author_url":data['author_url'],
            "html":data['html'],
            "pos": urls[i]["pos"]
        }
        jsonData.append(tmp)
    else:
        print('NG')

json.dump(jsonData, f)
f.close()
