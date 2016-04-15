###Sam Deslandes - Lab 8 

A total of 3 changes were made by our table: 
####Checkpoint 3 - Basic Queries
Basic queries such as:
	* `find()`
	* `findOne()`
	* `insert()`
	* `update()` 
![Basic Queries](https://www.dropbox.com/s/03n6ycoje5zur9z/Screenshot%202016-04-14%2023.17.53.png?dl=0)

####Checkpoint 4 - Python Queries
This checkpoint performs the same basic queries as checkpoint 3, this time driven by a pyhton script instead of directly through the monogo shell.  
![Checkpoint4 Output](https://www.dropbox.com/s/nx4jygc6sqxc9ab/Screenshot%202016-04-15%2000.49.18.png?dl=0)  

#####Code:  
```
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
```
 
####Checkpoint 5 - Random word script
This script prints a random word in the collection and its definition, as well as the dates it was accessed.  
![Checkpoint5 Output](https://www.dropbox.com/s/dbecbibq8g5ntw9/Screenshot%202016-04-15%2002.20.49.png?dl=0)  

#####Code:  
```
from pymongo import MongoClient
from random import randint
from datetime import datetime
client = MongoClient()
db = client.csci2963
collection = db.definitions

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    index = randint(0,collection.count()-1)
    collection.update({'word':collection.find()[index]['word']},
			  {'$push':{'dates':str(datetime.utcnow())}})
    doc = collection.find()[index]
    print("word: \"{}\"".format(doc['word']))
    print("defintion: \"{}\"".format(doc['definition']))
    print("dates: [{}]".format(', '.join(doc['dates'])))
    


if __name__ == '__main__':
    random_word_requester()

```
