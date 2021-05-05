from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

# Put
def add_playr(position, age, name):
	document = {
		'Position': position,
		'Age': age,
		'Name': name
	}
	return mycoll.insert_one(document)
player = add_playr('Midfielder', '22', 'Seamus Fleming')

