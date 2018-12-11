# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:09:35 2018

@author: Harsha Vardhan Manoj
"""
import re
import nltk
from urllib  import request
from bs4 import BeautifulSoup
url1="http://news.bbc.co.uk/2/hi/health/2284783.stm"
url2="http://www.nltk.org/"
def scores(url):
 try:
    page1=request.urlopen(url)
 except:
    print("\n could not open urls")
 nohtmlt=BeautifulSoup(page1,"lxml")
 title = nohtmlt.find('title')
 print('Title Of the page : ' + title.get_text())
 nohtml=nohtmlt.get_text()
 
 sents=nltk.sent_tokenize(nohtml)
 print(sents)
 words=0;
 letters=0;
 sentenses=0;
 for x in range(1, len(sents)-1):
    sentenses+=1;
    sent=sents[x];
    regex = r'(\w+) '
    list1=re.findall(regex,sent)
    words+=len(list1)
    for word in list1:
        letters+=len(word)
        
 ans1=(4.71*(letters/words)+0.5*(words/sentenses)-21.43)
 print("Site one:"+url)        
 print('No.of Sentnces:'+str(sentenses) )
 print('No.of words:'+str(words) )
 print('No.of letters:'+str(letters) )
 print("reading level score :"+str(ans1))

scores(url1)
print('======================')
scores(url2)      
    

