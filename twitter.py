# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:47:04 2018

@author: Harsha Vardhan Manoj
"""

import tweepy
import re

exec(open("TwitterTokens.py").read())

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

users = api.search_users("Villanova")


user_list = []

for i in users:
    user_list.append(i.id)

print(user_list)
timelines = []

for i in user_list:
    timelines.append(api.user_timeline(i))

print(timelines[0][0].created_at)
print(timelines[0][0].text)
print(timelines[0][0].retweet_count)
print(timelines[0][0].user.name)
print(timelines[0][0].user.id)



text = open("output.txt", "w")

for j in timelines:
    for i in j:
        string = str(i.user.name + "::" + str(i.user.id) + "::" + str(i.created_at) + "::" + str(i.retweet_count) + "::" + i.text)
        
        string = string.encode('utf-8')
        string = re.sub(r"^b'", '', str(string))
        string = re.sub(r"'$", '', str(string))
        string = re.sub(r'^b"', '', str(string))
        string = re.sub(r'"$', '', str(string))
        print(string)
        text.write(str(string) + '\n')
       

text.close()
        
    
    




