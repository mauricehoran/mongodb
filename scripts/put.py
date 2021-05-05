from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

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
