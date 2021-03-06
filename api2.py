import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    #Switchのproductid
    productid = "26ae34ea8f6c434c59fb74c7180565de"
    #https://webservice.rakuten.co.jp/api/ichibaitemsearch/参照
    #elements,カンマ区切りで出力pram指定
    #任意の商品の最高値、最低値を出力
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?productId={}&format=json&elements=maxPrice,minPrice&applicationId=1019079537947262807".format(productid)
    print(get_api(url))


main()
