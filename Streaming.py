import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import io
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "516928864-pBdqL0SdUFbvM646cDAltw6x3qQ9Eg6C2YVcnR6o"
access_token_secret = "t6gaIITThfh2neoTLYYk3UzI2QeAGROrrDZMfplpGnIdm"
consumer_key = "x09egWVUuPgRqxgPHI6lHJtlb"
consumer_secret = "vDMOfP8yeiKZszyXSpFzTQISEML0yv4otAKEDOwru5X3NCwpBk"

#start_time = time.time()
#keyword_list =  ['twitter']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):    
    def __init__(self, filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,keywords1,keywords2, keywords3,keywords4,keywords5,keywords6,keywords7,keywords8,time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        #self.fn = targetfilename
        #self.keywords = targetkeywords
        self.keywords1 = keywords1
        self.keywords2 = keywords2
        self.keywords3 = keywords3
        self.keywords4 = keywords4
        self.keywords5 = keywords5
        self.keywords6 = keywords6
        self.keywords7 = keywords7
        self.keywords8 = keywords8
        #self.out_file = open('tweets.json','a',encoding = 'utf-8')
        #self.out_file = open(targetfilename,'a',encoding = 'utf-8')
        self.out_file1 = open(filename1,'a',encoding = 'utf-8')
        self.out_file2 = open(filename2,'a',encoding = 'utf-8')
        self.out_file3 = open(filename3,'a',encoding = 'utf-8')
        self.out_file4 = open(filename4,'a',encoding = 'utf-8')
        self.out_file5 = open(filename5,'a',encoding = 'utf-8')
        self.out_file6 = open(filename6,'a',encoding = 'utf-8')
        self.out_file7 = open(filename7,'a',encoding = 'utf-8')
        self.out_file8 = open(filename8,'a',encoding = 'utf-8')
        #self.tweet_data = []
    
    def on_data(self, data):
        #print(data)
        temp=-1
        if(time.time()-self.start_time)<self.limit:
            #print(data['text'])
            parsed_data=json.loads(data)
            Check_exist = [False,False,False,False,False,False,False,False]
            Count = [0,0,0,0,0,0,0,0]
            keys =  parsed_data.keys()
            #print(keys)
            if 'text' in parsed_data:
                for i in parsed_data['text']:
                    if i in self.keywords1:
                        Check_exist[0] = True
                        Count[0] = Count[0]+1
                    if i in self.keywords2:
                        Check_exist[1] = True
                        Count[1] = Count[1]+1
                    if i in self.keywords3:
                        Check_exist[2] = True
                        Count[2] = Count[2]+1    
                    if i in self.keywords4:
                        Check_exist[3] = True
                        Count[3] = Count[3]+1
                    if i in self.keywords5:
                        Check_exist[4] = True
                        Count[4] = Count[4]+1
                    if i in self.keywords6:
                        Check_exist[5] = True
                        Count[5] = Count[5]+1
                    if i in self.keywords7:
                        Check_exist[6] = True
                        Count[6] = Count[6]+1
                    if i in self.keywords8:
                        Check_exist[7] = True
                        Count[7] = Count[7]+1

            maxindex = Count.index(max(Count))

            if(maxindex==0) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file1.write(data)
                self.out_file1.write("\n")
            if(maxindex==1) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file2.write(data)
                self.out_file2.write("\n")
            if(maxindex==2) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file3.write(data)
                self.out_file3.write("\n")
            if(maxindex==3) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file4.write(data)
                self.out_file4.write("\n")
            if(maxindex==4) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file5.write(data)
                self.out_file5.write("\n")
            if(maxindex==5) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file6.write(data)
                self.out_file6.write("\n")
            if(maxindex==6) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file7.write(data)
                self.out_file7.write("\n")
            if(maxindex==7) and Check_exist[maxindex] and Count[maxindex]>0:
                self.out_file8.write(data)
                self.out_file8.write("\n")
            temp=maxindex
            return True
        else:
            print(" Done")
            if(temp==0):
                self.out_file1.close()
            if(temp==1):
                self.out_file2.close()
            if(temp==2):
                self.out_file3.close()
            if(temp==3):
                self.out_file4.close()
            if(temp==4):
                self.out_file5.close()
            if(temp==5):
                self.out_file6.close()
            if(temp==6):
                self.out_file7.close()
            if(temp==7):
                self.out_file8.close()
            return False
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    happy_keyword=['happy','lol','great','awesome','cool','enjoying','funny','haha','hahaha','thank','like','good','beautiful','amazing','lovely','wonderful',':)',':-)','\U0001F600','\U0001F601','\U0001F602','\U0001F603','\U0001F604','\U0001F605','\U0001F606','\U0001F609','\U0001F60A','\U0001F60B','\U0001F60E','\U0001F60D','\U0001F617','\U0001F618','\U0001F619','\U0001F61A','\U0001F642','\U0001F917','\U0001F923','\U0001F638','\U0001F639','\U0001F63A']
    surprise_keyword=['surprise','omg','shocked','amazed','speechless','lost for words','astonished','jesus','holy','gosh','oh','god','wow','\U0001F631','\U0001F62E','\U0001F62F','\U0001F626','\U0001F640']
    sad_keyword=['sad','shit','fuck','fucking','fucked','disgraceful','blue','cry','upset','unhappy','poor','tragic','disaster','miss','disappointed','sorry','depressed','dejected','break','alone','hurt','miserable','mournful',':(','\U0001F622','\U0001F62D','\U0001F614','\u2639','\U0001F641','\U0001F612','\U0001F61E','\U0001F627','\U0001F494']
    anticipation_keyword=['will','happen','expected','expectation','hope','intent','intention','looking forward','contemplate','contemplation','prospect','happy','excited','\U0001F60D','\U0001F63B']
    love_keyword=['valentine','romantic','marry','engage','baby','bae','date','crush','relationship','ring','wedding','\U0001F60D','\U0001F618','\U0001F493','\U0001F495','\U0001F491']
    disgust_keyword=['disgusting','revolting','nasty','sick','infest','rotten','shitty','awful','repulsive','vomit','\U0001F644','\U0001F623','\U0001F62B','\U0001F616','\U0001F61F','\U0001F635','\U0001F637','\U0001F922','\U0001F92E']
    angry_keyword=['Angry','annoyed','mad','furious','fucking','piss','pissoff','piss off','hate','hate you','\U0001F620','\U0001F621','\U0001F624','\U0001F629','\U0001F612','\U0001F63E','\U0001F644','\U0001F643','\U0001F47F','\U0001F603']
    fear_keyword=['afraid','freak','scared','scary','nervous','paralyzed','terrifying','anxious','worried','pertrified','nightmare','\U0001F616','\U0001F623','\U0001F628','\U0001F631','\U0001F632','\U0001F635','\U0001F637','\U0001F64F','\U0001F648','\U0001F649','\U0001F64A','\U0001F633','\U0001F628']

    l = StdOutListener( "happy_tweets.json","surprise_tweets.json","sad_tweets.json","anticipation_tweets.json","love_tweets.json","disgust_tweets.json","angry_tweets.json","fear_tweets.json",happy_keyword,surprise_keyword,sad_keyword,anticipation_keyword,love_keyword,disgust_keyword,angry_keyword,fear_keyword,time_limit = 3600)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
   

    stream.filter(locations=[-124.1,23.7,-68.0,49.5],languages=['en'])













