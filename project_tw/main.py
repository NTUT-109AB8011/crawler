# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.moneycome.in/piggy/s/ci/calcStock"
    headers = {"accept" : "application/json",
               "Accept-Encoding" : "gzip, deflate, br",
               "Accept-Language" : "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6",
               "Connection" : "keep-alive",
               "Content-Length" : "333",
               #"Content-Type" : "application/json",
               "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
               "Cookie" : "_ga=GA1.2.1196452131.1613830558; __gads=ID=79e64714500465c3-229457f11ac600a7:T=1613830558:RT=1613830558:S=ALNI_MYl_j7I9GgUe3SxcvKDwBPgJrwLbA; _gid=GA1.2.434881184.1616354994; piggy_account_nickname=terranwu; piggy_account_token=4495451d712843cf5cdc19107c8abdeb06833b0cd4e2e4fb91819be16d67ce52329045d8d136212636c4fb3a81323d071519d6e3b57eaea79dfc9ca0ce2e187c; piggy_account_language=zh-TW; _gat_gtag_UA_56094162_5=1; _piggy_session=ZzB4OXdlbHZZbExKclJBenZxWXVEZjJoZU9aYXhyUWQxOWxSRXZzMXZPRk5tODVwUVhXN2tIUy9QZWovejRBZWxLc0poZGxyUTltakErdGpMaCtueVN5T1VQV3U0TTJ6VG9XdHNsSGJBd0JYT1RFSzRlT1p6T3R4VG92Q21ycVIrV0FmaHZHdXczd05hTlk5QmNCS3R3PT0tLWt1eFMvcUs1NWdhcFB6MnEyTWt0U1E9PQ==--7e8dbabffd5f84a9e054593a3d3d4f29db8f4d00",
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
                         data=dp
                        )
    print(resp.status_code)
    print(resp.request)
    print(resp.request.headers)
    print(resp.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
