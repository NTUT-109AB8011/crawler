import requests
import json
import csv
import re
from datetime import datetime as dt
from bs4 import BeautifulSoup as soup
#import Matplotlib
#import Pandas
#import NumPy

#def print_hi(name):
#    print(f'Hi, {name}')  # Print template

def upt_para(para, st, sy, ey) :
  para['stkCode'] = st
  para['startYear'] = sy
  para['endYear'] = ey
  
if __name__ == '__main__':
    print(dt.now())
    url_orig = "https://www.moneycome.in/tool/compound_interest?stkCode=5904"
    url_exep = "https://www.moneycome.in/piggy/s/ci/calcStock"
    para_exep = { "stkCode":"5904",
                "principle":1000000,
                "invAmtPerPeriod":60000,
                "startYear":2006,
                "endYear":2021,
                "isDividendReinvestment":True,
                "isCrashInvestment":False,
                "crashThreshold":0.3,
                "invAmtForCrash":60000}
    #Get supported stock list (done)
    resp_orig = requests.get(url_orig)
    resp_orig.raise_for_status()
    #print(resp_orig.text) #type : string
    page_orig = resp_orig.text
    soup_orig = soup(page_orig, "html.parser")
    #print(soup_orig.prettify())
    for script in soup_orig.find_all('script') :
     if re.search("g_stocks", str(script.string)):
        g_stocks = str(script.string)
        break
    #print (g_stocks)
    stock_list = re.findall(':"(.+)",' ,g_stocks)
    #print(stock_list)

    #Get expansion rate of each stock
    sd_l = []
    for st in stock_list:
      sd_d = {}
      print(st)
      for sy in range(2006, 2020) :
        for ey in range(2007, 2021) :
          if sy < ey :
            upt_para(para_exep, st, sy, ey)
            resp_exep = requests.post(url_exep, json=para_exep)
            resp_exep.raise_for_status()
            #print(resp.text) #type : string
            #print(st, sy, ey)
            sd_resp = json.loads(resp_exep.text) #stock_dict response
            if 'buyAtOpening' in sd_resp :
              bao = sd_resp['buyAtOpening']['yroi'].replace(' %', '')
            else :
              bao = None
            if 'buyAtHighest' in sd_resp :
              bah = sd_resp['buyAtHighest']['yroi'].replace(' %', '')
            else :
              bah = None
            if 'buyAtLowest' in sd_resp :
              bal  = sd_resp['buyAtLowest']['yroi'].replace(' %', '')
            else :
              bal = None
            if 'stkName' in sd_resp :
              stn  = sd_resp['stkName']
            else :
              stn = None
            #print (stn, bao, bah, bal)
            sd_d['id'] = st
            sd_d['name'] = stn
            sd_d['s'+str(sy)+'e'+str(ey)+'bao'] = bao
            sd_d['s'+str(sy)+'e'+str(ey)+'bah'] = bah
            sd_d['s'+str(sy)+'e'+str(ey)+'bal'] = bal
      sd_l.append(sd_d)
    # output JSON and CSV File
    # JSON & DICT format
    # [{id   : 5904,
    #  name: 寶雅,
    #  s2006e2007 : 26.7,
    #  .................,
    #  s2019e2020 : xxxx}
    #  {},
    #  {}
    # ]
    fn = 'stock_list.json'
    with open(fn, 'w', encoding='utf-8') as fnObj :
      json.dump(sd_l, fnObj, indent=2, ensure_ascii=False)

    #CSV format
    #id name s2006e2007 s2006e2008 ... s2006e2020 s2007e2008 ...s2007e2020 .. s2019e2020
    fn = 'stock_list.csv'
    with open(fn, 'w', newline = '', encoding='utf-8') as csvFile :
      fields = sd_l[o].keys
      print(type(fields))
      dicWriter = csv.DicWriter(csvFile, fieldnames = fields)
      dicWriter.writeheader()
      for row in sd_l :
       dicWriter.writerow(row)
      
    #TBD Begin
    #TBD End

    #Final Step
    #Animation for it
    #TBD Begin
    #TBD End

print('                  _            ')
print('                /`o\__         ')
print('         ,_     \ _.==\'        ')
print('        `) `----`~~\           ')
print('      -~ \  \'~-.   / ~-        ')
print('       ~- `~-====-\ ~_ ~-      ')
print('      ~ - ~ ~- ~ - ~ -         ')

print(dt.now())
