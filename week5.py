# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:26:36 2018

@author: Harsha Vardhan Manoj
"""

import re
import nltk
short_raw="DENNIS: Listen, strange women lying in ponds distributing swords is \n no basis for a system of government." 
wordlist=[w for w in nltk.corpus.words.words('en') if w.islower()]
print( re.findall('<as>+',['asasas','asssssssasa','fweffawqer']))

