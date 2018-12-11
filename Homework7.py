# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:51:18 2018

@author: Harsha Vardhan Manoj
"""

import pandas as pd
import re
import time
import numpy as np
udata = ['user_id', 'gender', 'age', 'occupation','zip']
users = pd.read_table('ml-latest-small/users.dat',sep='::',
                      header=None, names = udata, engine = 'python')
mdata=['movie_id', 'title', 'genre']
movies = pd.read_table('ml-latest-small/movies.dat', 
                       sep='::', header=None, names=mdata,engine = 'python')
rdata=['user_id','movie_id','rating','time']
ratings = pd.read_table('ml-latest-small/ratings.dat', 
                       sep='::', header=None, names=rdata,engine = 'python')

rating_years=[]

for rate in ratings['time']:
    rating_years.append(str(time.ctime(rate))[-4:]);
ratings['rating_year']=rating_years
data = pd.merge(pd.merge(ratings,users),movies)
#mean_ratings = data.pivot_table('rating',index=['title','rating_year'], aggfunc=[len, np.mean])
mean_ratings = data.pivot_table('rating',index=['title'], aggfunc=[len, np.mean])
pd.set_option('display.max_columns',50)
mean_ratings.reset_index(inplace=True)
#mean_ratings.columns = ['title', 'rating_year','no.of_Ratings','Mean']
mean_ratings.columns = ['title','no.of_Ratings','Mean']
years=[]
for movie in mean_ratings['title']:
    years.append(re.search('\(\d{4}\)',movie)[0]);
mean_ratings['year']=years
print("Movies with Year in their data")
print(mean_ratings)
print("===============================================================")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
mean_ratings=mean_ratings.loc[mean_ratings['no.of_Ratings'] >10]
print("Top movies:")
for x in range(1971, 2001):
   temp=pd.DataFrame(mean_ratings.loc[mean_ratings['year']=='('+str(x)+')'])
   print(temp.loc[temp['Mean']==temp['Mean'].max()])
   print("===============================================================")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
year_diff=[]

i=0;
prev=0;
top_movies=pd.DataFrame(mean_ratings.nlargest(20, 'Mean').sort_values(by=['year']))
for movie in top_movies['year']:
    if(i==0):
        prev=int(movie[1:5])
        year_diff.append(0)
        i=i+1
    else:
        year_diff.append(int(movie[1:5])-prev)
        prev=int(movie[1:5])
        

top_movies['Year_diff']= year_diff
print("===============================================================")
print("Top twenty movies")
print(top_movies)
print("===============================================================")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("average gap for release of top movies is")
print(str(top_movies['Year_diff'].mean())+'  Years')      
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")






 
   



