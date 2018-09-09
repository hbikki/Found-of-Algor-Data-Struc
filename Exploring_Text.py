# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:43:06 2018

@author: Harsha Vardhan Manoj
"""
#Ending in ize
#Containing the letter z
#Containing the sequence of letters pt
#Having all lowercase letters except for an initial capital (i.e., titlecase)
import nltk
from nltk.book import *
text = open("answer.txt","w")
Ending_in_ize=[]
Containing_letter_z=[]
Containing_sequence_pt=[]
Titlecase=[]
list_Tokens=list(text6)
for token in list_Tokens:
    length=len(token)
    if(length >= 3):
        if (token[length-1]=='e' and token[length-2]=='z' and token[length-3]=='i'):
            Ending_in_ize.append(token)
    if('z' in token):
        Containing_letter_z.append(token)
    if('p' in token and 't' in token):
        p_position=token.find('p')
        t_position=token.rfind('t');
        if(t_position > p_position):
            Containing_sequence_pt.append(token)
    if(token[0].isupper() and token[1:].islower()):
        Titlecase.append(token)
text.write("Tokens ending in \"ize\" are and no.of tokens are "+str(len(Ending_in_ize))+" :\n\n\n")
for print_token in Ending_in_ize:
    text.write(print_token+' , ');  
text.write("\n===================================================\n")
text.write("Tokens Containing letter z are and no.of tokens are "+str(len(Containing_letter_z))+" :\n\n\n")
for print_token in Containing_letter_z:
    text.write(print_token+' , ');  
text.write("\n===================================================\n")
text.write("Tokens sequence of letters pt are  and no.of tokens are "+str(len(Containing_sequence_pt))+" :\n\n\n")
for print_token in Containing_sequence_pt:
    text.write(print_token+' , ');  
text.write("\n===================================================\n")
text.write("Tokens Having all lowercase letters except for an initial capital are  and no.of tokens are "+str(len(Titlecase))+" :\n\n\n")
for print_token in Titlecase:
    text.write(print_token+' , ');  
text.write("\n===================================================")
text.close()        

