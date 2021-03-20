import urllib.request as request
with request.urlopen(xxx) as response
  data = response.read()
print(data)
