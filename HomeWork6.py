# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:08:55 2018

@author: Harsha Vardhan Manoj
"""
import pandas as pd
names1990 = pd.read_csv("baby\yob1990.txt",names = ['name','sex','births'])
print(" most common boy’s name in 1900 :\n")
print(names1990.loc[names1990['births'].idxmax()])
#name=input('enter name:\n');
#sex=input('enter gender:\n');
years = range(1880,2018)
pieces = []
columns = ['name','sex','births']
path = 'baby/yob1880.txt'   
frame = pd.read_csv(path,names=columns)    
frame['year'] = 1800
pieces.append(frame) 
print(pieces)
#for year in years:   
#    path = 'baby/yob%d.txt' %year   
#    frame = pd.read_csv(path,names=columns)    
#    frame['year'] = year
#    pieces.append(frame) 

#names = pd.concat(pieces, ignore_index=True)
#print(names)
#data=names.loc[(names['name'] == name) & (names['sex'] == sex)]
#print(data.loc[data['births'].idxmax()])
#total_births = data.pivot_table('births',index='year')
#total_births.plot(title="Total births with name+"+name+"in all years")
#
#enteredyear=input('enter year:\n');
#yeardat= pd.read_csv("baby\yob"+enteredyear+".txt",names = ['name','sex','births'])
#yeardata1=yeardat[yeardat['sex'] == 'F']
#print('Female top 25 in '+enteredyear+' :\n')
#print(yeardata1.nlargest(25,'births'))
#yeardata2=yeardat[yeardat['sex'] == 'M']
#print('Male top 25 '+enteredyear+' :\n')
#print(yeardata2.nlargest(25,'births'))
