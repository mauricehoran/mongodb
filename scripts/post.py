from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

#  Post
mycoll.update_many({'Position': 'Goalkeeper'}, {'$set': {'Position': 'Goalie'}})

