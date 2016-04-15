from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()
db = client.csci2963 #get db
collection = db.definitions #get collection

if __name__ == '__main__':
    collection.delete_many({'word':'brainpower'})#to avoid duplicates when inserting
    print("find()")
    for definition in collection.find():
	print(definition)    
    
    print("\nfind_one()")
    print(collection.find_one())
    
    print("\nfind(<match here>)")
    print("For this example match 'word:Capitalland'")
    for match in collection.find({"word":"Capitaland"}):
    	print(match)
    print("\nNow match id 56fe9e22bad6b23cde07b8ce")
    for match in collection.find({"_id":ObjectId('56fe9e22bad6b23cde07b8ce')}):
    	print(match)

    print("\nLastly, insert")
    print("Before insert: search for word 'brainpower' returns {}".format(collection.count({'word':'brainpower'})))
    print("Insert Here")
    collection.insert_one({'word':'brainpower','definition':'O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA'})
    print("After insert: {}".format(collection.count({'word':'brainpower'})))
