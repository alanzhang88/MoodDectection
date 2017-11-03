# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:38:47 2017

@author: admin
"""

import csv 
import json
#import sys 
import re

import os

folderpath = "C:/WendyCui/CS145/project/data/stream_data" #folder's path
files= os.listdir(folderpath) #get all the files' name in the folder

#regular representation#
try:# Wide UCS-4 build
    myre = re.compile(u'['
                      u'\U0001F300-\U0001F64F'
                      u'\U0001F680-\U0001F6FF'
                      u'\u2600-\u2B55]+',
                      re.UNICODE)
except re.error:# Narrow UCS-2 build
    myre = re.compile(u'('
                      u'\ud83c[\udf00-\udfff]|'
                      u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                      u'[\u2600-\u2B55])+',
                      re.UNICODE)

for file in files: 
     if not os.path.isdir(file): #if it is not a folder, open it
         #jsonData = open(folderpath + "/" + file) #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行 
         txtfile = open(folderpath + "/" + file)
         csvfile = open(folderpath + "/" + file[:-4] + '.csv', 'w',newline='')
         selected_keys = ['created_at','favorite_count','retweet_count','id_str','location','followers_count','friends_count','listed_count','favourites_count','verified','statuses_count','label']
         tweet_keys = ['created_at','favorite_count','retweet_count']
         user_keys = ['id_str','location','followers_count','friends_count','listed_count','favourites_count','verified','statuses_count']
         #lines = jsonData.readlines()
         lines2 = txtfile.readlines()
         writer = csv.DictWriter(csvfile,selected_keys)
         writer.writeheader()
         mood = file[:-4]
         label_value = 0
         if(mood == 'happy'):
             label_value = 3
         elif(mood == 'love'):
             label_value = 2
         elif(mood == 'anticipation'):
             label_value = 1
         elif(mood == 'surprise'):
             label_value = 0
         elif(mood == 'disgust'):
             label_value = -1
         elif(mood == 'fear'):
             label_value = -2
         elif(mood == 'anger'):
             label_value = -2.5
         elif(mood == 'sad'):
             label_value = -3
         
         label_dict = {'label':label_value}
         for line in lines2:
             line = line.strip() #remove space at line head and tail 
             if not len(line) or line.startswith('#'): #remove lines without content and note line
                continue
             if (line.find('created_at') == -1): #remove unuseful line
                continue
             dic = json.loads(line)
             user_dict = dict((key, value) for key, value in dic['user'].items() if key in user_keys)
             tweet_dict = dict((key, value) for key, value in dic.items() if key in tweet_keys)
             #unicode filter for dict values#
             if(user_dict != {} and tweet_dict != {}):
                 for user_key in user_dict.keys():
                     temp = str(user_dict[user_key]).encode("GBK",'ignore')
                     temp = temp.decode("GBK",'ignore')
                     user_dict[user_key] = myre.sub('',temp)
                 for tweet_key in tweet_dict.keys():
                     temp = str(tweet_dict[tweet_key]).encode("GBK",'ignore')
                     temp = temp.decode("GBK",'ignore')
                     tweet_dict[tweet_key] = myre.sub('',temp)
                 
                 final_dict = {**tweet_dict,**user_dict,**label_dict}
                 writer.writerow(final_dict)
         csvfile.close()
         txtfile.close()
          #jsonData.close()
