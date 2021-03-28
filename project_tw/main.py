import requests
import json
import csv
import re
import time
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
    url_orig = "https://www.moneycome.in/tool/compound_interest?stkCode=6533"
    url_exep = "https://www.moneycome.in/piggy/s/ci/calcStock"
    para_exep = { "stkCode":"6533",
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
    fn_jsn = 'stock_list.json'
    try:
      with open(fn_jsn, 'r', encoding='utf-8') as fnObj :
        sd_l = json.load(fnObj)
    except Exception :
      sd_l = []
    for i, st in enumerate(stock_list, start=0):
      #if i < 0 :
      #  continue
      #elif i > 5 :
      #  break
      sd_d = {}
      print(i, st)
      for sy in range(2006, 2021) :   #2006~2020
        for ey in range(2007, 2022) : #2007~2021
          if sy < ey :
            upt_para(para_exep, st, sy, ey)
            retry = True
            while retry :
              try :
                resp_exep = requests.post(url_exep, json=para_exep)
                resp_exep.raise_for_status() #REVIST, need redo if received "Bad request'
                retry = False
              except:
                print('Well, let\'s take a rest: 60s')
                time.sleep(60)

            #print(resp.text) #type : string
            print(st, sy, ey)
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
            print (stn, bao, bah, bal)
            sd_d['id'] = st
            sd_d['name'] = stn
            sd_d['s'+str(sy)+'e'+str(ey)+'bao'] = bao
            sd_d['s'+str(sy)+'e'+str(ey)+'bah'] = bah
            sd_d['s'+str(sy)+'e'+str(ey)+'bal'] = bal
      sd_l.append(sd_d)
    # output JSON and CSV File
    # JSON & DICT format
    # [{id   : 6533,
    #  name: 晶心科,
    #  s2006e2007 : 26.7,
    #  .................,
    #  s2019e2020 : xxxx}
    #  {},
    #  {}
    # ]
    with open(fn_jsn, 'w', encoding='utf-8') as fnObj :
      json.dump(sd_l, fnObj, indent=2, ensure_ascii=False)

    #CSV format
    #id name s2006e2007 s2006e2008 ... s2006e2020 s2007e2008 ...s2007e2020 .. s2019e2020
    fn_csv = 'stock_list.csv'
    with open(fn_csv, 'w', newline = '', encoding='utf-8') as csvFile :
      fields = sd_l[0].keys()
      #print(type(fields))
      dictWriter = csv.DictWriter(csvFile, fieldnames = fields)
      dictWriter.writeheader()
      for row in sd_l :
        dictWriter.writerow(row)
      
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
