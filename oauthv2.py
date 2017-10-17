import oauth2 as oauth
import json

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
token = oauth.Token(access_token,access_token_secret)

client = oauth.Client(consumer,token)

#twitter_api_test_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

#resp, content = client.request(twitter_api_test_url,"GET")
#print resp
#print content
'''
twitter_api_friend_list = "https://api.twitter.com/1.1/friends/list.json"

resp, content = client.request(twitter_api_friend_list,"GET")

content = json.loads(content)
print resp
print content['next_cursor']
for user in content['users']:
    print user['id']
    print user["name"]
'''

test_user_id = '1542453360'

twitter_api_uri = "https://api.twitter.com"

#twitter_api_user_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json"
twitter_api_user_timeline = "/1.1/statuses/user_timeline.json?user_id=%s&count=200" % test_user_id
print twitter_api_user_timeline
twi_url = twitter_api_uri + twitter_api_user_timeline
print twi_url

resp,content = client.request(uri=twi_url,method='GET')
print resp
print type(content)
#print content


content = json.loads(content)
for t in content:
    print t["created_at"]
    print t["id"]
    print t["text"]

'''
twitter_statues_filter = "https://stream.twitter.com/1.1/statuses/filter.json?track=happy"
resp,content = client.request(twitter_statues_filter,"GET")
print resp
print content
'''

