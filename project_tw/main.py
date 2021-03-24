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
    url = "https://www.moneycome.in/piggy/s/ci/calcStock"
    headers = {"Accept" : "application/json",
               "Accept-Encoding" : "gzip, deflate, br",
               "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "Connection" : "keep-alive",
               "Content-Length": "333",
               "content-type" : "application/json",
               "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
               "Cookie" : "piggy_account_nickname=terranwu; piggy_account_token=4495451d712843cf5cdc19107c8abdeb06833b0cd4e2e4fb91819be16d67ce52329045d8d136212636c4fb3a81323d071519d6e3b57eaea79dfc9ca0ce2e187c; piggy_account_language=zh-TW; _gat_gtag_UA_56094162_5=1; _piggy_session=ZzB4OXdlbHZZbExKclJBenZxWXVEZjJoZU9aYXhyUWQxOWxSRXZzMXZPRk5tODVwUVhXN2tIUy9QZWovejRBZWxLc0poZGxyUTltakErdGpMaCtueVN5T1VQV3U0TTJ6VG9XdHNsSGJBd0JYT1RFSzRlT1p6T3R4VG92Q21ycVIrV0FmaHZHdXczd05hTlk5QmNCS3R3PT0tLWt1eFMvcUs1NWdhcFB6MnEyTWt0U1E9PQ==--7e8dbabffd5f84a9e054593a3d3d4f29db8f4d00",
               "Host" : "www.moneycome.in",
               "Origin" : "https://www.moneycome.in",
               "sec-ch-ua" : '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
               "sec-ch-ya-mobile" : "?0",
               "Sec-Fetch-Dest" : "empty",
               "Sec-Fetch-Mode" : "cors",
               "Sec-Fetch-Site" : "same-origin",
               "Referer" :"https://www.moneycome.in/tool/compound_interest?stkCode=5904"}
    dp = {"token":"4495451d712843cf5cdc19107c8abdeb06833b0cd4e2e4fb91819be16d67ce52329045d8d136212636c4fb3a81323d071519d6e3b57eaea79dfc9ca0ce2e187c",
          "stkCode":"5904",
          "principle":1000000,
          "invAmtPerPeriod":60000,
          "startYear":2006,
          "endYear":2021,
          "isDividendReinvestment":True,
          "isCrashInvestment":False,
          "crashThreshold":0.3,
          "invAmtForCrash":60000}
    resp = requests.post(url,
                         headers=headers,
                         #data=dp
                         json=dp
                        )
    resp.raise_for_status()
    #print(resp.status_code)
    #print(resp.request)
    #print(resp.request.headers)
    print(resp.text)
    print(type(resp.text))
    
    stock_dict = json.loads(resp.text)
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
