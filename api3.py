import requests
import urllib
import csv
import json


def get_api(url):
    result = requests.get(url)
    return result.json()


def exp_csv(data):
    with open("./rakuten_apidata.csv", mode="a") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["ランク","商品名","価格"])
        for line in data:
            writer.writerow([line["rank"],line["itemName"],line["itemPrice"]])
            print(line["rank"],line["itemName"],line["itemPrice"])



def main():
    #https://webservice.rakuten.co.jp/api/ichibaitemsearch/参照
    #elements,カンマ区切りで出力pram指定
    #20代女性のランキング,rank,アイテム名,価格
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?&applicationId=1019079537947262807&age=20&sex=1&elements=itemName,itemPrice,rank&formatVersion=2"
    get_data = get_api(url)
    #csvに格納
    exp_csv(get_data["Items"])
main()
