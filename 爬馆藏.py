import requests
import re


def esu(bookid):
  url = "https://findcumt.libsp.com/find/physical/groupitems"
  payload = {"page":1,"rows":20,"entrance":None,"recordId":bookid,"isUnify":True}
  headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Content-Length': '71',
  'Content-Type': 'application/json;charset=UTF-8',
  'groupCode': '200069',
  'Referer': 'https://findcumt.libsp.com/',
  'Cookie': 'SameSite=None'
}

  response = requests.request("GET", url, headers=headers, json=payload)

  return response.text

def search_location(result):
    location=re.findall(',"locationName":(.+?|null),',result)
    return location

def search_barcode(result):
    barcode=re.findall(',"barcode":(.+?|null),',result)
    return barcode

def search_attribution(result):
    attribution=re.findall(',"processType":(.+?|null),',result)
    return attribution
def s_id(result):
    bookid=re.findall(',"processType":(.+?|null),',result)
    return bookid

cout=input()
result=esu(cout)
location=search_location(result)
barcode=search_barcode(result)
attribution=search_attribution(result)
bookid=s_id(result)
sum=[]
for i in range(len(bookid)):
    temporary={"书的id":bookid[i],"条码":barcode[i],"放在哪里":location[i],"是否在架":attribution[i],"这是第几条馆藏信息":i+1}
    sum.append(temporary)
print(sum)