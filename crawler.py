import json
import oauth2 as oauth
import time
import random
import config

consumer_key=config.consumer_key
consumer_secret=config.consumer_secret

access_token=config.access_token
access_token_secret=config.access_token_secret

infin_loop = config.infin_loop
expand_times = config.expand_times

def retrieve_tweets(client,user_id,logfile):
    twitter_url = ("https://api.twitter.com/1.1/statuses/user_timeline.json?user_id=%s&count=200" % user_id)
    print("Requesting for timeline for user %s..." % user_id)
    logfile.write("Requesting for timeline for user %s...\n" % user_id)
    resp, content = client.request(uri=twitter_url,method="GET")
    if resp['status'] == "200":
        print("Succeeded in retrieving tweets, writing to file...")
        logfile.write("Succeeded in retrieving tweets, writing to file...\n")
        filename = "./data/%s.txt" % user_id
        f = open(filename,'w')
        f.write(content)
        f.close()
        return True
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


consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
token = oauth.Token(access_token,access_token_secret)
                    
client = oauth.Client(consumer,token)
#x_rate_remain = "15"
#x_rate_reset = ""

log = open('crawl_log.log','a')
x_rate_remain,x_rate_reset = retrieve_rates(client,log)
meta = open('./data/user.txt','r')
print("Opening metainfo file user.txt for read...")
log.write("Opening metainfo file user.txt for read...\n")
last = ''
count = 0
user_set = set()
for line in meta.readlines():
    last = line.strip('\n')
    count += 1
    user_set.add(last)

meta.close()
print("Finished reading metafile with %d users and the last user is %s..." % (count,last))
log.write("Finished reading metafile with %d users and the last user is %s...\n" % (count,last))
meta = open('./data/user.txt','a')

retrieve_tweets(client,last,log)

to_search = list()
to_search.append(last)

while infin_loop == True or expand_times > 0:
    if(x_rate_remain=="0"):
        print("x-rate-remain:0")
        log.write("x-rate-remain:0\n")
        reset = long(x_rate_reset)
        now = long(time.time())
        if(now<reset):
            print("Sleeping for %d" % (reset - now))
            log.write("Sleeping for %d\n" % (reset - now))
            time.sleep(reset-now)

    if len(to_search)==0:
        to_search = random.sample(user_set,min(2,len(user_set)))

    to_search_id = to_search.pop(0)
    id_list, x_rate_remain, x_rate_reset = retrieve_friends(client,to_search_id,log)
    if(len(id_list)==0):continue
    id_sample = random.sample(id_list,min(2,len(id_list)))
    for id in id_sample:
        if str(id) not in user_set:
            print("Gain a new user:%s" % str(id))
            log.write("Gain a new user:%s\n" % str(id))
            res = retrieve_tweets(client,str(id),log)
            if res:
                meta.write(str(id)+"\n")
                user_set.add(str(id))
                to_search.append(str(id))
        else:
            print("Found a old user:%s" % str(id))
            log.write("Found a old user:%s\n" % str(id))
            to_search.append(str(id))
    if expand_times > 0: expand_times -= 1

meta.close()
log.close()

