from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

# Delete
mycoll.delete_many({'Position': 'Forward'})
for result in mycoll.find():
        print(result)
print()
