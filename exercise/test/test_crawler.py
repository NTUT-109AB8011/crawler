import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
  #data = response
  #data = response.read()
  #data = response.read().decode("utf-8")
  data = json.load(response)
  #data = json.loads(response.read().decode("utf-8"))

clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
  for company in clist:
    file.write(company["公司地址"]+"\n")
  #print (addr_dict)
  #print (addr_dict["公司名稱"])
  #print (addr_dict["公司地址"])
