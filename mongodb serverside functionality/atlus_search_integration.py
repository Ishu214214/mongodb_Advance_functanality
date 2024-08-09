from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"


client = MongoClient(CONNECTION_STRING)


pipeline = [
  {
    "$search": {
      "index": "default",
      "text": {
        "query": "ubuy_B0CSFLGQ8T",
        "path": {
         "wildcard": "*",
        },
      },
    },
  },
]


result = client.copy_example.copy_example.aggregate(pipeline)


for doc in result:
    print(doc)
    print(f"\033[34m" + "*" * 10 + " ishu " + "*" * 10 + "\033[0m")
    print()

 







    """https://cloud.mongodb.com/v2/65f549c95822a42afcb44d33#/metrics/replicaSet/65f54ac49fd85449dbd90248/explorer/copy_example/copy_example/find
    """



