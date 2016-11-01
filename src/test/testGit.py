#!C:\Anaconda2\python.exe
'''
Created on 2016_11_02

@author: jeanus
'''

import urllib
import socket
import time


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

symbols = list()
file_object = open(r'E:\Be_A_Quant\MoneyFloatStrategy\stocks.txt')
for line in file_object:
    symbols.append(line.strip())
print len(symbols)

output = open(r"E:\Be_A_Quant\MoneyFloatStrategy/webpage.txt", 'w+')

socket.setdefaulttimeout(5)

for symbol in symbols:
    try:
        print symbol
        url = "http://data.eastmoney.com/zjlx/"+symbol+".html"
        html = getHtml(url)
        output.write(html+"\n")
        output.flush()
        time.sleep(0.4) 
    except Exception,ex:
        print Exception,":",ex
        time.sleep(2) 
        
output.close()
