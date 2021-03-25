# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
from bs4 import BeautifulSoup as soup
#import Matplotlib
#import Pandas
#import NumPy

#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
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
    resp_orig = requests.get(url_orig)
    print(resp_orig.text)
    soup_orig = soup(resp_orig.text, features="html.parser")

    #Get expansion rate of each stock, 5904 first
    resp_exep = requests.post(url_exep,
                              json=para_exep
                             )
    resp_exep.raise_for_status()
    #print(resp.text) #type string
    
    stock_dict = json.loads(resp_exep.text)
    exp_buyAtOpening = stock_dict['buyAtOpening']['yroi'].replace(' %', '')
    exp_buyAtHighest = stock_dict['buyAtHighest']['yroi'].replace(' %', '')
    exp_buyAtLowest  = stock_dict['buyAtLowest']['yroi'].replace(' %', '')
    print (exp_buyAtOpening, exp_buyAtHighest, exp_buyAtLowest)

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

    #Final Step
    #Animation for it
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
