# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:28:26 2020

@author: yniu
"""

import requests
from bs4 import BeautifulSoup
import re
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a :
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
            
        except:
            continue
    for l in range(len(lst)):
        print(lst[l])
        
    
def getstockInfo(lst, stockurl, fpath):
#    count = 0
    for stock in lst:
        url = stockURL + stock+".html"
        html = getHTMLText(url)
        try:
            if html =="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'htmp.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            
            infoDict.update({'Stock Name': name.text.split()[0]})
            
            keylist = stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                infoDict[key] = val
                
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
 #               count = count + 1
 #               print(\r'Curret: {:.2f}%'.format(count*100/len(lst)), end='')         
        except:
#            count = count + 1
#            print(\r'Curret: {:.2f}%'.format(count*100/len(lst)), end='')
#            traceback.print_exc()
            continue
    return ""

def main():
    slist = []
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 
    getStockList(slist, stock_list_url)
    

main()    
    
    
    
    