# MongoDB Pipeline Script
from pymongo import MongoClient
myclient = MongoClient('172.17.0.2',27017)
mydb = myclient["mauricedb"]
mycoll = mydb["mhcoll"]

myList = [
	{'Name': 'Sean Buckley', 'Age': '29', 'Position': 'Forward'},
	{'Name': 'Lee Keegan', 'Age': '30', 'Position': 'Defender'},
	{'Name': 'Stephen Lavin', 'Age': '32', 'Position': 'Defender'},
	{'Name': 'Pat Murphy', 'Age': '22', 'Position': 'Midfielder'},
	{'Name': 'John Galvin', 'Age': '22', 'Position': 'Goalkeeper'},
	{'Name': 'Mike Horan', 'Age': '32', 'Position': 'Defender'},
	{'Name': 'Sean Horan', 'Age': '32', 'Position': 'Goalkeeper'},
	{'Name': 'Timmy Horan', 'Age': '32', 'Position': 'Defender'},
	{'Name': 'Timmy Jones', 'Age': '29', 'Position': 'Forward'},
	{'Name': 'Mikey Smith', 'Age': '30', 'Position': 'Defender'},
	{'Name': 'Seanie Buckley', 'Age': '32', 'Position': 'Forward'},
	{'Name': 'Pa Ranahan', 'Age': '22', 'Position': 'Defender'}
]

x = mycoll.insert_many(myList)
