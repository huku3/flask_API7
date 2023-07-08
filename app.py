import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=3720038")
#文字型なのでエラーが起きる
# print(res.text["status"]) 
# print(type(res.text))
# print(type(res.json()))
# print(res.json()["status"])
print(res.json()["results"][0]["address1"])
print(res.json()["results"][0]["address2"])
print(res.json()["results"][0]["kana1"])
print(res.json()["results"][0]["kana2"])
print(res.json()["results"][0]["kana3"])
print(res.json()["results"][0]["prefcode"])
print(res.json()["results"][0]["zipcode"])
