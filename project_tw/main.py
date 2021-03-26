import requests
import json
import re
from bs4 import BeautifulSoup as soup
#import Matplotlib
#import Pandas
#import NumPy

#def print_hi(name):
#    print(f'Hi, {name}')  # Print template

if __name__ == '__main__':
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
    #Get supported stock list
    #TBD Begin
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
    print (g_stocks)
     

    #TBD End

    #Get expansion rate of each stock, 5904 first
    resp_exep = requests.post(url_exep,
                              json=para_exep
                             )
    resp_exep.raise_for_status()
    #print(resp.text) #type : string
    
    stock_dict = json.loads(resp_exep.text)
    exp_buyAtOpening = stock_dict['buyAtOpening']['yroi'].replace(' %', '')
    exp_buyAtHighest = stock_dict['buyAtHighest']['yroi'].replace(' %', '')
    exp_buyAtLowest  = stock_dict['buyAtLowest']['yroi'].replace(' %', '')
    print (exp_buyAtOpening, exp_buyAtHighest, exp_buyAtLowest)

    #output CSV and JSON File
    #CSV format
    #ID name f2006t2007 f2006t2008 ... f2006t2020 f2007t2008 ...f2007t2020 .. f2019t2020
    #JSON & DICT format
    #[{id   : 5904,
    #  cname: 寶雅,
    #  f2006t2007 : 26.7,
    #  .................,
    #  f2019t2020 : xxxx}
    #  {},
    #  {}
    # ]
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

