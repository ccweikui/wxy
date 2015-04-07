#-*- coding=utf8 -*-
import csv
import cPickle

SPLIT_NUMBER = 50
users = {}
for index,line in enumerate(open('tianchi_mobile_recommend_train_user.csv')):
	if index == 0:
		continue
	#if index > 10000:
	#	break
	lines = line.split(",")
	(user_id,item_id,behavior_type,user_geohash,item_category,time) = lines
	if not user_id in users:
		users[user_id] = []
	users[user_id].append(lines)
length = len(users)
print length
tmpUsers = {}
for index,userid in enumerate(users):
	for i in range(1,SPLIT_NUMBER+1):
		tmpUsers[userid] = users[userid]
		if index == length*i/SPLIT_NUMBER-1:
			print index
			fileName = "output/users_%s" % i
			f = open(fileName,"w+")
			cPickle.dump(tmpUsers,f)
			tmpUsers = {}
			f.close()
