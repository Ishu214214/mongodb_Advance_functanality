
import time
import pymongo
import sys
import datetime
"""  for write operation    """
CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/?readPreference=primaryPreferred&retryWrites=true" 

"""
for read operation
CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/?readPreference=secondaryPreferred" 

"""
client = pymongo.MongoClient(CONNECTION_STRING)
mydatabase = client['copy_last_id_hello'] 
mycollection=mydatabase['copy_ubuy_last_hello'] 



# """     insert """
for i in range(1):

    result = mycollection.insert_many([{"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}] , ordered= False)
    print("Inserted IDs:", result.inserted_ids)
    time.sleep(2)

""" update """
# myquery = { "name": "aaa" }
# newvalues = { "$set": { "address": "Canyon 12345" } }
# mycollection.update_one(myquery, newvalues)

client.close()