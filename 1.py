from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

# Get
print("### All entries in the collection ###")
for result in mycoll.find():
        print(result)
print()

# Put
def add_player(name, age, position):
	document = {
		'Name': name,
		'Age': age,
		'Position': position
	}
	print("###", name, " has been added ###")
	return mycoll.insert_one(document)

player = add_player("Timmy Horan", '32', 'Forward')
print()

#  Post
mycoll.update_many({'Position': 'Goalkeeper'}, {'$set': {'Position': 'Goalie'}})



# Delete
mycoll.delete_one({'Position': 'Forward'})
for result in mycoll.find():
        print(result)
print()





# Insert many
# Delete many
# Query
