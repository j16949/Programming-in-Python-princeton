
from stockaccount import StockAccount
import sys
import stockquote
from instream import InStream
import stdio
import os

stockAccounts = list()
 
path = './accounts'  
result=os.listdir(path)
n =len(result)
loser = ''
winner = ''
wtotal = 0
ltotal = float("inf")

for i in range(n):
    stockAccounts.append(StockAccount(path+'/'+result[i]))

for i in range(n):
    v = stockAccounts[i].valueOf()
    if v > wtotal:
        wtotal = v
        winner = stockAccounts[i]._name
    if v < ltotal:
        ltotal = v
        loser = stockAccounts[i]._name

print('The biggest winner is ',winner)
print('The biggest loser is ',loser)

#--------------------------------------------
#python3 winnerAndLoser.py 

