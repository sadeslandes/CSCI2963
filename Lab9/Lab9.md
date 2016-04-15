###Sam Deslandes - Lab 8 

####Checkpoint 3 - Basic Queries
Basic queries such as:  
- `find()`  
- `findOne()`  
- `insert()`  
- `update()`   
![Basic Queries](http://puu.sh/oiNI8/21c238ae72.png)

####Checkpoint 4 - Python Queries
This checkpoint performs the same basic queries as checkpoint 3, this time driven by a pyhton script instead of directly through the monogo shell.  
![Checkpoint4 Output](http://puu.sh/oiNJ0/f6a501035a.png)  

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
![Checkpoint5 Output](http://puu.sh/oiNJt/b1fdf05e22.png)  

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
