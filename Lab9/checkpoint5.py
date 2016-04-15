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
