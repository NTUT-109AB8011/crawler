#!/opt/homebrew/bin/python3
#import mymodule

#mymodule.greeting("Jonathan")
#import platform
#x=platform.system()
#print(x)
#import datetime

#x = datetime.datetime.now()
#print(x)
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
