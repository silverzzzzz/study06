import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    #https://webservice.rakuten.co.jp/api/ichibaitemsearch/参照
    #elements,カンマ区切りで出力pram指定
    #任意の商品の最高値、最低値を出力
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?&applicationId=1019079537947262807"
    print(get_api(url))


main()
