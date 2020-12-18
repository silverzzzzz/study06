import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = input("キーワードを入力してください>>>")
    #https://webservice.rakuten.co.jp/api/ichibaitemsearch/参照
    #elements,カンマ区切りで出力pram指定
    #商品名itemName,価格itemPrice
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&elements=itemName,itemPrice&applicationId=1019079537947262807".format(
        keyword)
    print(get_api(url))


main()
