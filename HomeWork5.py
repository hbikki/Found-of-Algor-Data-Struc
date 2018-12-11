# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:01:08 2018

@author: Harsha Vardhan Manoj
"""

from nltk.corpus import words
words=words.words()
word_list=[low.lower() for low in words]
import re
text = open("hw5text.txt","rt")
s=text.read()
print(s)
w=re.findall("\S+-\n\S+",s)
print(w)
for i in range (len(w)): 
  smallword1=re.sub('\n',"",w[i])
  smallword2=re.sub('-\n|-',"",w[i])
  if(smallword1 in word_list):
      print('is a valid word :'+smallword1)
  else:
      split=smallword1.split('-')
      checker=True
      for i in range (len(split)):
          if split[i].lower().strip() in word_list:
              checker=True
              continue
          else:
              checker=False
              break 
      if(checker):
          print('is a valid word :'+smallword1)
      else:
          print(smallword1+'  is not valid word it should be changed to :'+smallword2) 

text.close()
