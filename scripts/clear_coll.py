from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

# Delete
mycoll.delete_one({'Position': 'Forward'})
mycoll.delete_one({'Position': 'Goalkeeper'})
mycoll.delete_one({'Position': 'Goalie'})
mycoll.delete_one({'Position': 'Defender'})
mycoll.delete_one({'age': '29'})
mycoll.delete_one({'age': '30'})
mycoll.delete_one({'Name': 'Pa Ranahan'})
mycoll.delete_one({'Name': 'Stephen Lavin'})
mycoll.delete_one({'Name': 'Mike Horan'})
mycoll.delete_one({'Name': 'Sean Horan'})
mycoll.delete_one({'Name': 'Timmy Jones'})
mycoll.delete_one({'Name': 'Seanie Buckley'})
mycoll.delete_one({'Name': 'Mikey Smith'})
mycoll.delete_one({'Name': 'Timmy Horan'})
mycoll.delete_one({'Position': 'Midfielder'})
for result in mycoll.find():
        print(result)
print()

