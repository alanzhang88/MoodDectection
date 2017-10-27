import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import io
#import json

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#start_time = time.time()
#keyword_list =  ['twitter']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):    
    def __init__(self, time_limit = 60):
        self.start_time = time.time()
        self.limit = time_limit
        self.out_file = open('tweets.json','a',encoding = 'utf-8')
        #self.tweet_data = []
    
    def on_data(self, data):
        #print(data)
        if(time.time()-self.start_time)<self.limit:
            self.out_file.write(data)
            self.out_file.write("\n")

            return True
        else:
            print("Done")
            self.out_file.close()
            return False
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener( time_limit = 20)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['happy'])