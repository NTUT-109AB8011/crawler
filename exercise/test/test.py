#!/opt/homebrew/bin/python3

#print("Hello World!")
#stock = 'tsmc'
#close = 217.5
#print(f'{stock} price: {close}')
##tsmc price: 217.5'
#def maxx(*value):
#  if len(value) > 0:
#    tmax = value[0]
#  else :
#    tmax = 0
#  for next in value[1:] :
#    if next > tmax:
#      tmax = next
#  return tmax
#
#print(maxx(1,2,3,4,5))
#print(maxx())
#import camelcase
#
##c = camelcase.CamelCase()
##
##txt = "hello world"
##
##print(c.hump(txt))
#x = "hello"
#
#if not type(x) is int:
#  #raise TypeError("Only integers are allowed")
#  raise Exception("Only integers are allowed")
#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk

mypath = "."

# 
for root, dirs, files in walk(mypath):
  print("root", root)
  print("dirs", dirs)
  print("files", files)
