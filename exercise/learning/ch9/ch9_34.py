# ch9_34.py
season = {'水瓶座':'1月20日 - 2月18日, 須警惕小人',
          '雙魚座':'2月19日 - 3月20日, 凌亂中找立足',
          '白羊座':'3月21日 - 4月19日, 運勢比較低迷',
          '金牛座':'4月20日 - 5月20日, 財運較佳',
          '雙子座':'5月21日 - 6月21日, 運勢好可錦上添花',
          '巨蟹座':'6月22日 - 7月22日, 不可鬆懈大意',
          '獅子座':'7月23日 - 8月22日, 會有成就感',
          '處女座':'8月23日 - 9月22日, 會有挫折感',
          '天秤座':'9月23日 - 10月23日, 運勢給力',
          '天蠍座':'10月24日 - 11月22日, 中規中矩',
          '射手座':'11月23日 - 12月21日, 可羨煞眾人',
          '魔羯座':'12月22日 - 1月19日, 需保有謙虛',
          }

wd = input("請輸入欲查詢的星座 : ")
if wd in season:
    print(wd, " 本月運勢 : ", season[wd])
else:
    print("星座輸入錯誤")













