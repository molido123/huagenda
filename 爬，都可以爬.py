from types import BuiltinMethodType
import requests
import re

def esu(searchid,page):
   url = "https://findcumt.libsp.com/find/unify/search"
   payload ={"docCode":[None],"searchFieldContent":searchid,"searchField":"keyWord","matchMode":"2","resourceType":[],"subject":[],"discode1":[],"publisher":[],"libCode":[],"locationId":[],"eCollectionIds":[],"curLocationId":[],"campusId":[],"kindNo":[],"collectionName":[],"author":[],"langCode":[],"countryCode":[],"publishBegin":None,"publishEnd":None,"coreInclude":[],"ddType":[],"verifyStatus":[],"group":[],"sortField":"relevance","sortClause":"asc","page":page,"rows":10,"onlyOnShelf":None,"indexSearch":1,"searchItems":None}
   headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'groupCode': '200069',
  'Host': 'findcumt.libsp.com',
  'Referer': 'https://findcumt.libsp.com/',
   'Cookie': 'SameSite=None; SameSite=None'
  }
   response = requests.request("POST", url, headers=headers, json=payload )
   return response.text

def introduction(result):
    introduction=re.findall('"adstract":(".+?"|null),"dd',result)
    return introduction

def simplify_bookid(result):
    recordid=re.findall('"recordId":([0-9]*?),"fa',result)
    return recordid

def simplify_name(result):
    name=re.findall('"title": (".+?"),"co',result)
    return name    

def simplify_author(result):
    author=re.findall('"author":(".+?"|null)',result)
    return author

def simplify_publisher(result):
    publisher=re.findall('"publisher":(".+?"|null),"is',result)
    return publisher

def simplify_isbn(result):
    isbn=re.findall('"isbn":(".+?"|null),"isbns',result)
    return isbn

print("请输入‘搜索目标 页数’" )
INPUT=input().split()
searchid=INPUT[0]
page=INPUT[1]
result=esu(searchid,page)
recordid=simplify_bookid(result)
author=simplify_author(result)
publisher=simplify_publisher(result)
brief=introduction(result)
isbn=simplify_isbn(result)
sum=[]
N=len(recordid)
for i in range(N):
  temporary={"bookid":recordid[i],"author":author[i],"出版社":publisher[i],"isbn":isbn[i],"简介":brief[i],"第几本书":i+1}
  sum.append(temporary)
print(sum)
print("本页记录数")
print(len(sum))
print("page")
print(page)
print("想具体看哪本书,输入一个数字")
check=int(input())
print(sum[check-1])