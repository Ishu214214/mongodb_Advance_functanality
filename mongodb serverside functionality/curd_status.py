from pymongo import MongoClient
from datetime import datetime, timedelta
from pymongo import ReadPreference
from bson.timestamp import Timestamp

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
mydatabase = client['copy_last_id'] 
mycollection = mydatabase['copy_ubuy_last_id1'] 
audit_log_collection = mydatabase['audit_log']

start_date = datetime.now() 

admin_db = client.admin
server_status = mydatabase.command("serverStatus")
opcounters = server_status["opcounters"]
print(opcounters)
print(server_status.keys())



"""
https://www.mongodb.com/docs/manual/core/replica-set-oplog/
https://www.mongodb.com/community/forums/t/how-to-get-the-count-for-all-the-crud-operations-on-a-collection-for-the-last-2-days/9803
"""

client = MongoClient(CONNECTION_STRING, read_preference=ReadPreference.PRIMARY)
database_name = 'copy_last_id'
collection_name = 'copy_ubuy_last_id1'

local_db = client.local

start_ts = Timestamp(int((datetime.now() - timedelta(days=2)).timestamp()), 0)

pipeline = [
    {"$match": {"ts": {"$gt": start_ts}, "ns": f"{database_name}.{collection_name}"}},
    {"$group": {"_id": "$op", "count": {"$sum": 1}}}
]

# Execute the aggregation pipeline on the oplog collection
result = local_db.oplog.rs.aggregate(pipeline)


for doc in result:
    print(doc)
