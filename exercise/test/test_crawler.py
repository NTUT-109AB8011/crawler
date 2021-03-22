#import sleep
#import urllib.request as request
#import json
#src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
#with request.urlopen(src) as response:
#  #data = response
#  #data = response.read()
#  #data = response.read().decode("utf-8")
#  data = json.load(response)
#  #data = json.loads(response.read().decode("utf-8"))
#
#clist = data["result"]["results"]
#with open("data.txt", "w", encoding="utf-8") as file:
#  for company in clist:
#    file.write(company["公司地址"]+"\n")
#  #print (addr_dict)
#  #print (addr_dict["公司名稱"])
#  #print (addr_dict["公司地址"])
#time.sleep(4)
#
#import urllib.request as req
#def getData(url):
#  #print(url)
#  request=req.Request(url, headers={
#    "cookie" : "over18=1",
#    "User-Agent": "(Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36)"
#  })
#  with req.urlopen(request) as response:
#    data=response.read().decode("utf-8")
#  #print(data)
#  import bs4
#  root=bs4.BeautifulSoup(data, "html.parser")
#  #print(root.title)
#  #print(root.title.string)
#  titles=root.find_all("div", class_="title")
#  #print(titles)
#  #print(titles.a)
#  #print(titles.a.string)
#  for title in titles:
#    if title.a != None:
#      print(title.a.string)
#  
#  nextlink=root.find("a", string="‹ 上頁")
#  #print(nextlink)
#  return nextlink["href"]
#
#pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
#count=0
#while count<3:
#  pageURL="https://www.ptt.cc"+getData(pageURL)
#  count+=1

#import urllib.request as req
#url="https://www.moneycome.in/tool/compound_interest?stkCode=5904"
#request=req.Request(url, headers={
#  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
#})
#with req.urlopen(request) as response:
#  data=response.read().decode("utf-8")
#print(data)

import requests
url= 'https://www.moneycome.in/piggy/s/ci/calcStock'
dp = {"token":"4495451d712843cf5cdc19107c8abdeb06833b0cd4e2e4fb91819be16d67ce5279c5a8a7fa01c2b9d539f7fbb9edce63a1d253bee07fb8967227b3478aeaa53d","stkCode":"5904","principle":1000000,"invAmtPerPeriod":60000,"startYear":2006,"endYear":2021,"isDividendReinvestment":true,"isCrashInvestment":false,"crashThreshold":0.3,"invAmtForCrash":60000}
x = requests.get(url, headers={
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
data=dp
})
print (x.text)
