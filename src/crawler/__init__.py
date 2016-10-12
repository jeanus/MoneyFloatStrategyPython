#coding:utf-8

import urllib
import socket
import time

from bs4 import BeautifulSoup


def getHtml(url):
    page = urllib.urlopen(url).read()
    return page

date = "2016-10-10"
timeout = 10
socket.setdefaulttimeout(timeout)

symbols = list()
file_object = open(r'E:\360_Quant\Quant_Strategy\Be_A_Quant\MoneyFloatStrategy\stocks_today.txt')
for line in file_object:
    symbols.append(line.strip())
print len(symbols)

        

output = open(r"E:\360_Quant\Quant_Strategy\Be_A_Quant\MoneyFloatStrategy\money_float_1012.txt", 'w+')
'''
for symbol in symbols:
    if symbol=='300138':
        try:
            url = "http://data.eastmoney.com/zjlx/"+symbol+".html"
            html = getHtml(url)
            soup = BeautifulSoup(html,from_encoding="gb18030" )
            div = soup.find_all("div",{"class":"flash-data-cont flash-data-cont-line"})[0]
            line = "0"+"\t"+date
            if symbol.startswith("6"):
                stock = "sh"+symbol
            else:
                stock = "sz"+symbol
            url = "http://hq.sinajs.cn/list="+stock
            wp = urllib.urlopen(url)
            content = str(wp.read())
            pre_close = float(content.split(",")[2])
            today_close = float(content.split(",")[3])
            change = str(round(100*(today_close/pre_close-1),2))+"%"
            line = line +"\t"+str(today_close)+"\t"+change
            i = 0
            for span in div.find_all(name='span'):
                if i%2==0:
                    line = line +"\t"+span.string+"万"
                else:
                    line = line +"\t"+span.string
                i= i+1
            output.write(symbol+"\n")
            output.write(line+"\n")
            output.write("\n")
            output.flush()
            time.sleep(0.1)  
        except Exception,ex:
            print "Find Error "+ symbol
            print Exception,":",ex
            time.sleep(2) 
output.close()
'''
while len(symbols)>0:
    error_list = list()
    for symbol in symbols:
        try:
            # print symbol+" ",
            url = "http://data.eastmoney.com/zjlx/"+symbol+".html"
            html = getHtml(url)
            soup = BeautifulSoup(html,from_encoding="gb18030" )
            table = soup.find_all(name='table')[1]
            trs = (soup.find_all(name='table')[1].find_all(name='tr',onmouseover="this.className='over'"))
            output.write(symbol+"\n")
            offset = 0
            for tr in trs:
                output.write(str(offset)+"\t")
                tds = tr.find_all(name='td')[0]
                output.write(tds.string.strip()+"\t")
                tds = tr.find_all(name='span')
                for td in tds:
                    output.write(td.string+"\t")
                output.write("\n")      
                offset = offset - 1
                if offset==-1:
                    break;
            output.write("\n")            
            output.flush()
            time.sleep(0.1) 
        except Exception,ex:
            error_list.append(symbol)
            print "Find Error "+ symbol
            print Exception,":",ex
            time.sleep(2) 
    symbols = error_list



