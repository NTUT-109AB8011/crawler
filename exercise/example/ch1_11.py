# ch1_11.py
import json

fn = 'login.json'
login = input("請輸入帳號 : ")
with open(fn, 'w') as fnObj:
    json.dump(login, fnObj) #dump no s, dump to file
    print("%s! 歡迎使用本系統! " % login)
    print("fnObj type", type(fnObj))

login2 = "test2"
jason2Data = json.dumps(login2) #dumps, dump to string
print("jason2Data", jason2Data)
print("jason2Data type", type(jason2Data))
