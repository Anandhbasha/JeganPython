import math

print(math.sqrt(25))
print(math.pow(2,4)) # 2*2*2*2
print(math.pi)

import random 
print(random.random())
print(random.randint(99999,1000000))
print(random.choice(["red","blue","Yellow"]))

import datetime

thisday = datetime.date.today()
print(thisday)

timeNow = datetime.datetime.now()
print(timeNow)

import os

print(os.name)
# print(os.getcwd())
# os.mkdir("Images")

import sys
print(sys.version)


import json

data = {"name":"abc","age":20}
print(type(data))

jString = json.dumps(data)
print(type(jString))

newValue = json.loads(jString)
print(type(newValue))

# regular expression
# re
import re 

text = "this is my number7895454545"
num = r'\d{10}'
match = re.search(num,text)
if match:
    print("Number found",match.group())

from Excepton import greet

greet()