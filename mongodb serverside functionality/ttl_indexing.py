import time
import pymongo
import datetime
CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
client = pymongo.MongoClient(CONNECTION_STRING)
mydatabase = client['copy_last_id'] 
mycollection=mydatabase['copy_ubuy_last_id'] 

"""     change the time in ttl index    """
#mydatabase.command("collMod", "copy_ubuy_last_id", index={'keyPattern': {"inserted": 1}, 'expireAfterSeconds': 1})

"""     create the ttl index    """
#mycollection.create_index("inserted", expireAfterSeconds = 5)

inserted_id1 = mycollection.insert_one({"order_number":12345678, "last_id":datetime.datetime.utcnow()}).inserted_id
print(inserted_id1)
i = 1
while mycollection.find_one(inserted_id1) is not None:
    time.sleep(2)
    i += 1

print(i)
exit()

