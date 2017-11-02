import ast
import json
from collections import Counter
import os
from pathlib import Path

def load_file(file_name):
	with open(file_name,'r') as f:
		read_data = f.read()
	f.closed
	data = []
	if(read_data):
		data = json.loads(read_data)
	return data

def classify(json_obj):
	text = json_obj["text"]
	text_lower = text.lower()
	words = text_lower.split()
	c = Counter(words)
	# add more emoji for happy later
	count_happy = c["lol"] + c["happy"] + c["great"]+ c["awesome"]+ c["cool"]+ c["enjoying"]+ c["funny"]+ c["haha"]+ c["hahaha"]+ c["thank"]+ c["like"]+ c["good"]+ c["beautiful"]+ c["amazing"]+ c["lovely"]+ c["wonderful"]+ c[":)"]+ c[":-)"]+ c["u1f600"]+ c["u1f601"]+ c["u1f602"]+ c["u1f603"]
	count_love = c["valentine"]+ c["romantic"]+ c["marry"]+ c["engage"]+ c["baby"]+ c["bae"]+ c["dating"]+ c["crush"]+ c["relationship"]+ c["ring"]+ c["wedding"]+ c["u1f60d"]+ c["u1f618"]+ c["u1f493"]+ c["u1f495"]+ c["u1f491"]
	count_anticipation = c["expect"]+ c["hope"]+ c["intent"]+ c["intention"]+ c["expectation"]+ c["forward"]+ c["contemplate"]+ c["contemplation"]+ c["prospect"]+ c["u1f60d"]+ c["u1f63b"]
	count_surprise = c["surprise"]+ c["omg"]+ c["shocked"]+ c["amazed"]+ c["speechless"]+ c["astonished"]+ c["jesus"]+ c["holy"]+ c["gosh"]+ c["oh"]+ c["god"]+ c["wow"]+ c["u1f631"]+ c["u1f62e"]+ c["u1f62f"]+ c["u1f626"]+ c["u1f640"]
	count_disgust = c["disgusting"]+ c["disgust"]+ c["revloting"]+ c["nasty"]+ c["sick"]+ c["infest"]+ c["rotten"]+ c["shitty"]+ c["awful"]+ c["repulsive"]+ c["vomit"]
	count_fear = c["afraid"]+ c["freak"]+ c["scared"]+ c["nervous"]+ c["paralyzed"]+ c["terrifying"]+ c["anxious"]+ c["worried"]+ c["pertrified"]+ c["nightmare"]+ c["u1f616"]+ c["u1f623"]+ c["u1f628"]+ c["u1f631"]+ c["u1f632"]+ c["u1f635"]+ c["u1f637"]+ c["u1f640"]+ c["u1f64f"]+ c["u1f648"]+ c["u1f649"]+ c["u1f64a"]+ c["u1f633"]+ c["u1f628"]
	count_anger = c["angry"]+ c["annoyed"]+ c["mad"]+ c["furious"]+ c["fucking"]+ c["pissoff"]+ c["hate"]+ c["u1f620"]+ c["u1f621"]+ c["u1f624"]+ c["u1f629"]+ c["u1f63e"]+ c["u1f644"]+ c["u1f643"]+ c["u1f67f"]+ c["u1f603"]
	count_sad = c["sad"]+ c["cry"]+ c["upset"]+ c["unhappy"]+ c["poor"]+ c["tragic"]+ c["disaster"]+ c["miss"]+ c["disappointed"]+ c["sorry"]+ c["depressed"]+ c["dejected"]+ c["break"]+ c["alone"]+ c["hurt"]+ c["hurts"]+ c["miserable"]+ c["mournful"]+ c[":("]+ c["u1f622"]+ c["u1f62d"]+ c["u1f614"]+ c["u2639"]+ c["u1f641"]+ c["u1f612"]+ c["u1f61e"]+ c["u1f627"]+ c["u1f494"]
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

def filter(user_id):
	filename = "./data/%s.txt" % user_id
	data = load_file(filename)
	count = 0
	if(len(data)==0):
		return 0
	else:
		for json_obj in data:
			classfier = classify(json_obj)
			if(classfier != 0):
				count += 1
			if(classfier==1):
				with open('./filter_data/happy.txt','a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==2):
				with open('./filter_data/love.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==3):
				with open('./filter_data/anticipation.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==4):
				with open('./filter_data/surprise.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==5):
				with open('./filter_data/disgust.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==6):
				with open('./filter_data/fear.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==7):
				with open('./filter_data/anger.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
			if(classfier==8):
				with open('./filter_data/sad.txt', 'a') as outfile:
					json.dump(json_obj, outfile)
					outfile.write('\n')
				outfile.closed
		return count;


if __name__ == '__main__':
	meta = open('./data/user.txt','r')
	print("Opening metainfo file user.txt for read...")
	for line in meta.readlines():
		last = line.strip('\n')
		filename = "./data/%s.txt" % last
		print("Opening ",filename, " to filter...")
		count = filter(last)
		print("Successfully filter ", count, " Json objects from ", filename, "...")
	meta.close()
