import json
import oauth2 as oauth
import time
import random
import os
import config
from pathlib import Path
from collections import Counter

consumer_key=config.consumer_key
consumer_secret=config.consumer_secret

access_token=config.access_token
access_token_secret=config.access_token_secret

infin_loop = config.infin_loop
expand_times = config.expand_times
target_location = config.target_location
sample_size = config.sample_size


def classify(json_obj):
    text = json_obj["text"]
    text_lower = text.lower()
    count_happy = 0
    count_love = 0
    count_anticipation = 0
    count_surprise = 0
    count_disgust = 0
    count_fear = 0
    count_anger = 0
    count_sad = 0
    count_happy += text_lower.count(u"\U0001F600")+ text_lower.count(u"\U0001F601")+text_lower.count(u"\U0001F602")+ text_lower.count(u"\U0001F603")+text_lower.count(u"\U0001F604")+text_lower.count(u"\U0001F605")+text_lower.count(u"\U0001F606")+text_lower.count(u"\U0001F60A")+text_lower.count(u"\U0001F60B")+text_lower.count(u"\U0001F60E")+text_lower.count(u"\U0001F60D")+text_lower.count(u"\U0001F618")
    count_love += text_lower.count(u"\U0001F60D")+ text_lower.count(u"\U0001F618")+ text_lower.count(u"\U0001F617")+ text_lower.count(u"\U0001F619")+ text_lower.count(u"\U0001F61A")+ text_lower.count(u"\U0001F63B")+ text_lower.count(u"\U0001F9D6")+ text_lower.count(u"\U0001F48F")+ text_lower.count(u"\U0001F469")+ text_lower.count(u"\U0001F48B")+ text_lower.count(u"\U0001F498")+ text_lower.count(u"\U0001F493")+ text_lower.count(u"\U0001F495")+ text_lower.count(u"\U0001F496")+ text_lower.count(u"\U0001F497")+ text_lower.count(u"\U0001F499")
    count_anticipation += text_lower.count(u"\U0001F60D")+ text_lower.count(u"\U0001F63B")
    count_surprise += text_lower.count(u"\U0001F631")+ text_lower.count(u"\U0001F62E")+ text_lower.count(u"\U0001F62F")+ text_lower.count(u"\U0001F626")+ text_lower.count(u"\U0001F640")
    count_disgust += text_lower.count(u"\U0001F922")+ text_lower.count(u"\U0001F92E")+ text_lower.count(u"\U0001F4A9")
    count_fear += text_lower.count(u"\U0001F616")+ text_lower.count(u"\U0001F623")+ text_lower.count(u"\U0001F628")+ text_lower.count(u"\U0001F631")+ text_lower.count(u"\U0001F632")+ text_lower.count(u"\U0001F635")+ text_lower.count(u"\U0001F637")+ text_lower.count(u"\U0001F640")+ text_lower.count(u"\U0001F64F")+ text_lower.count(u"\U0001F648")+ text_lower.count(u"\U0001F649")+ text_lower.count(u"\U0001F64A")+ text_lower.count(u"\U0001F633")+ text_lower.count(u"\U0001F628")
    count_anger += + text_lower.count(u"\U0001F620") + text_lower.count(u"\U0001F621")+ text_lower.count(u"\U0001F624")+ text_lower.count(u"\U0001F629")+ text_lower.count(u"\U0001F63E")+ text_lower.count(u"\U0001F644")+ text_lower.count(u"\U0001F643")+ text_lower.count(u"\U0001F47F")
    count_sad += text_lower.count(u"\U0001F622")+ text_lower.count(u"\U0001F614")+ text_lower.count(u"\U0001F61E")+ text_lower.count(u"\U0001F494")
    if(text_lower.find("looking forward") != -1):
        count_anticipation += 1
    if(text_lower.find("lost for words") != -1):
        count_surprise += 1
    words = text_lower.split()
    c = Counter(words)
    count_happy += c["lol"] + c["happy"] + c["awesome"]+ c["haha"]+ c["hahaha"]+ c["thank"]+ c["amazing"]+ c[":)"]+ c[":-)"] +c[":D"]
    count_love += c["valentine"]+ c["romantic"]+ c["marry"]+ c["engage"]+ c["baby"]+ c["bae"]+ c["dating"]+ c["crush"]+ c["relationship"]+ c["ring"]+ c["wedding"]
    count_anticipation += c["expect"]+ c["expectation"]+ c["hope"]+ c["intent"]+ c["intention"]+ c["contemplate"]+ c["contemplation"]+ c["prospect"]+ c["excited"]+ c["thank"]+ c["amazing"]
    count_surprise += c["surprise"]+ c["omg"]+ c["shocked"]+ c["amazed"]+ c["speechless"]+ c["astonished"]+ c["jesus"]+ c["holy"]+ c["gosh"]+ c["oh"]+ c["god"]+ c["wow"]
    count_disgust += c["disgusting"]+ c["disgust"]+ c["revloting"]+ c["nasty"]+ c["sick"]+ c["infest"]+ c["rotten"]+ c["shitty"]+ c["awful"]+ c["repulsive"]+ c["vomit"]+ c["disgust"]
    count_fear += c["afraid"]+ c["haunted"]+ c["ghost"]+c["freak"]+ c["horror"]+ c["scared"]+ c["scary"]+ c["nervous"]+ c["terrifying"]+ c["anxious"]+ c["worried"]+ c["nightmare"]
    count_anger += c["angry"]+ c["annoyed"]+ c["mad"]+ c["furious"]+ c["fucking"]+ c["piss"]+ c["hate"]+c["shuts"]+c["shut"]+c["fuck"]+c["annoying"]
    count_sad += c["sad"]+ c["cry"]+ c["upset"]+ c["unhappy"]+ c["poor"]+ c["tragic"]+ c["disaster"]+ c["disappointed"]+ c["sorry"]+ c["break"]+ c["alone"]+ c["hurt"]+ c["hurts"]+ c["miserable"]+ c[":("]
    # 0 for nothing, 1 happy, 2 love, 3 anticipation, 4 surprise, 5 disgust, 6 fear, 7 anger, 8 sad
    if(count_happy==0 and count_love==0 and count_anticipation==0 and count_surprise==0 and count_disgust==0 and count_fear==0 and count_anger==0 and count_sad==0):
        return 0
    elif(count_happy>count_love and count_happy>count_anticipation and count_happy>count_surprise and count_happy>count_disgust and count_happy>count_fear and count_happy>count_anger and count_happy>count_sad):
        return 1
    elif(count_love>count_happy and count_love>count_anticipation and count_love>count_surprise and count_love>count_disgust and count_love>count_fear and count_love>count_anger and count_love>count_sad):
        return 2
    elif(count_anticipation>count_happy and count_anticipation>count_love and count_anticipation>count_surprise and count_anticipation>count_disgust and count_anticipation>count_fear and count_anticipation>count_anger and count_anticipation>count_sad):
        return 3
    elif(count_surprise>count_love and count_surprise>count_anticipation and count_surprise>count_happy and count_surprise>count_disgust and count_surprise>count_fear and count_surprise>count_anger and count_surprise>count_sad):
        return 4
    elif(count_disgust>count_love and count_disgust>count_anticipation and count_disgust>count_surprise and count_disgust>count_happy and count_disgust>count_fear and count_disgust>count_anger and count_disgust>count_sad):
        return 5
    elif(count_fear>count_love and count_fear>count_anticipation and count_fear>count_surprise and count_fear>count_disgust and count_fear>count_happy and count_fear>count_anger and count_fear>count_sad):
        return 6
    elif(count_anger>count_love and count_anger>count_anticipation and count_anger>count_surprise and count_anger>count_disgust and count_anger>count_fear and count_anger>count_happy and count_anger>count_sad):
        return 7
    elif(count_sad>count_love and count_sad>count_anticipation and count_sad>count_surprise and count_sad>count_disgust and count_sad>count_fear and count_sad>count_anger and count_sad>count_happy):
        return 8
    else:
        return 0

def filter(data):
    count = 0
    if(len(data)==0):
        return 0
    else:
        for json_obj in data:
            classfier = classify(json_obj)
            if(classfier != 0):
                count += 1
            if(classfier==1):
                with open('./data/happy.txt','a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==2):
                with open('./data/love.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==3):
                with open('./data/anticipation.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==4):
                with open('./data/surprise.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==5):
                with open('./data/disgust.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==6):
                with open('./data/fear.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==7):
                with open('./data/anger.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
            if(classfier==8):
                with open('./data/sad.txt', 'a') as outfile:
                    json.dump(json_obj, outfile)
                    outfile.write('\n')
                outfile.closed
        return count;

def location_filter(input_tweet,target_loc):
    if input_tweet['user']['location'] == None:
        return False
    input_loc = input_tweet['user']['location']
    for loc in target_loc:
        if loc in input_loc:
            return True
    return False

def retrieve_tweets(client,user_id,logfile,myfilter=None):
    twitter_url = ("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=%s&count=200" % user_id)
    print("Requesting for timeline for user %s..." % user_id)
    logfile.write("Requesting for timeline for user %s...\n" % user_id)
    resp, content = client.request(uri=twitter_url,method="GET")
    if resp['x-rate-limit-remaining'] == "0":
        print("x-rate-remain for retrieve tweet is 0")
        log.write("x-rate-remain for retrieve tweet is 0\n")
        reset = long(resp['x-rate-limit-reset'])
        now = long(time.time())
        if(now<reset):
            print("Sleeping for %d" % (reset - now + 5))
            log.write("Sleeping for %d\n" % (reset - now + 5))
            time.sleep(reset-now+5)

    if resp['status'] == "200":
        if myfilter == None:
            print("Succeeded in retrieving tweets, writing to file...")
            logfile.write("Succeeded in retrieving tweets, writing to file...\n")
            #filename = "./data/%s.txt" % user_id
            ####added####
            j = []
            if(content):
                j = json.loads(content)
                count_filter = filter(j)
                print_str = "Successfully filter %d tweets from %d tweets..." % (count_filter,len(j))
                print(print_str)
                logfile.write(print_str)
            ####added#####
            #f = open(filename,'w')
            #####
            #if isinstance(content,str):
            #    f.write(content)
            #else:
            #    f.write(str(content))
            #####

            #f.close()
            return True
        else:
            print("Succeeded in retrieving tweets, entering filter...")
            logfile.write("Succeeded in retrieving tweets, entering filter...\n")
            j = json.loads(content)
            if len(j)==0:
                print("Empty tweets, skipping the user...")
                logfile.write("Empty tweets, skipping the user...\n")
                return False
            ret = myfilter(j[0],target_location)
            if ret:
                print("Passed the filter, writing to files...")
                logfile.write("Passed the filter, writing to files...\n")
                count_filter = filter(j)
                print_str = "Successfully filter %d tweets from %d tweets..." % (count_filter,len(j))
                print(print_str)
                logfile.write(print_str)
                #filename = "./data/%s.txt" % user_id
                #f = open(filename,'w')
                #if isinstance(content,str):
                #    f.write(content)
                #else:
                #    f.write(str(content))
                #f.close()
                return True
            else:
                print("Failed the filter, skipping the user...")
                logfile.write("Failed the filter, skipping the user...\n")
                return False

    else:
        print("Failed in retrieving tweets")
        print("status:%s" % resp['status'])
        print("X-rate-remain:%s" % resp['x-rate-limit-remaining'])
        return False

def retrieve_friends(client,user_id,logfile):
    twitter_url = "https://api.twitter.com/1.1/friends/ids.json?cursor=-1&user_id=%s&count=5000" % user_id
    print("Requesting for friendslist for user %s..." % user_id)
    logfile.write("Requesting for friendslist for user %s...\n" % user_id)
    resp, content = client.request(uri=twitter_url,method="GET")
    idlist = list()
    if resp['status'] == "200":
        print("Succeeded in retrieving friendslist")
        logfile.write("Succeeded in retrieving friendslist\n")
        content = json.loads(content)
        idlist = content['ids']
    else:
        print("Failed in retrieving friendlist")
        print("status:%s" % resp['status'])
        print("X-rate-remain:%s" % resp['x-rate-limit-remaining'])
    return idlist, resp['x-rate-limit-remaining'], resp['x-rate-limit-reset']


def retrieve_rates(client,logfile):
    twitter_rate_limit = "https://api.twitter.com/1.1/application/rate_limit_status.json?resources=friends"
    print("Requesting for rate limits info...")
    logfile.write("Requesting for rate limits info...\n")
    resp,content = client.request(uri=twitter_rate_limit,method="GET")
    if resp['status'] == '200':
        print("Succeeded in retrieving rate limits info...")
        logfile.write("Succeeded in retrieving rate limits info...\n")
        content = json.loads(content)
        print("Current rate:%s" % content['resources']['friends']['/friends/ids']['remaining'])
        print("Current reset:%s" % content['resources']['friends']['/friends/ids']['reset'])
        logfile.write("Current rate:%s\n" % content['resources']['friends']['/friends/ids']['remaining'])
        logfile.write("Current reset:%s\n" % content['resources']['friends']['/friends/ids']['reset'])
        return content['resources']['friends']['/friends/ids']['remaining'],content['resources']['friends']['/friends/ids']['reset']
    else:
        print("Failed in retrieving rate limits info...")
        return "-1","-1"


consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
token = oauth.Token(access_token,access_token_secret)

client = oauth.Client(consumer,token)
#x_rate_remain = "15"
#x_rate_reset = ""

log = open('crawl_log.log','a')
x_rate_remain,x_rate_reset = retrieve_rates(client,log)
if x_rate_remain == "-1":
    print("Terminate since failing to retrieve the rate infomation.")
    quit()

#added
visited_user = []
visited_file = Path('./data/visited_user.txt')
if visited_file.is_file():
	with open('./data/visited_user.txt', 'r') as visited:
		for line in visited.readlines():
			last = line.strip('\n')
			visited_user.append(last)
	visited.closed
#added
meta = open('./data/user.txt','r')
print("Opening metainfo file user.txt for read...")
log.write("Opening metainfo file user.txt for read...\n")
last = ''
count = 0
user_set = set()
for line in meta.readlines():
    last = line.strip('\n')
    count += 1
    if (last in visited_user):
        print("Data for %s has already exist" % last)
        user_set.add(last)
    else:
        print("Data for %s is not found, Requesting tweets from twitter" % last)
        ret_status = retrieve_tweets(client,last,log,location_filter)
        if ret_status:
            user_set.add(last)
            visited = open('./data/visited_user.txt', 'a')
            visited.write(last+'\n')
            visited.close()
    #filename = "./data/%s.txt" % last
    #p = Path(filename)
    #if p.is_file():
    #    print("Data for %s has already exist" % last)
    #    user_set.add(last)
    #else:
    #    print("Data for %s is not found, Requesting tweets from twitter" % last)
    #    ret_status = retrieve_tweets(client,last,log,location_filter)
    #    if ret_status:
    #        user_set.add(last)
meta.close()

if count > len(user_set):
    print("Filtered out %d user in the orginal user meta file" % (count-len(user_set)))
    meta = open('./data/user.txt','w')
    for u in user_set:
        meta.write(u+'\n')
    meta.close()
    count = len(user_set)

print("Finished reading metafile with %d users and the last user is %s..." % (count,last))
log.write("Finished reading metafile with %d users and the last user is %s...\n" % (count,last))
meta = open('./data/user.txt','a')
visited = open('./data/visited_user.txt', 'a')
#retrieve_tweets(client,last,log,location_filter)

to_search = list()
to_search.append(last)

while infin_loop == True or expand_times > 0:
    if(x_rate_remain=="0"):
        print("x-rate-remain:0")
        log.write("x-rate-remain:0\n")
        reset = long(x_rate_reset)
        now = long(time.time())
        if(now<reset):
            print("Sleeping for %d" % (reset - now + 5))
            log.write("Sleeping for %d\n" % (reset - now + 5))
            time.sleep(reset-now+5)

    if len(to_search)==0:
        to_search = random.sample(user_set,min(sample_size,len(user_set)))

    to_search_id = to_search.pop(0)
    id_list, x_rate_remain, x_rate_reset = retrieve_friends(client,to_search_id,log)
    if(len(id_list)==0):continue
    id_sample = random.sample(id_list,min(sample_size,len(id_list)))
    for id in id_sample:
        str_id = str(id)
        if str_id not in user_set:
            print("Gain a new user:%s" % str_id)
            log.write("Gain a new user:%s\n" % str_id)
            res = retrieve_tweets(client,str_id,log,location_filter)
            if res:
                user_set.add(last)
                meta.write(str_id+"\n")
                visited.write(str_id+"\n")
                to_search.append(str_id)
        else:
            print("Found a old user:%s" % str_id)
            log.write("Found a old user:%s\n" % str_id)
            to_search.append(str_id)
    if expand_times > 0: expand_times -= 1

visited.close()
meta.close()
log.close()
