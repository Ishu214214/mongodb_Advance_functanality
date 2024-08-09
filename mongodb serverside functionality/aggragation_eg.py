import pymongo

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
client = pymongo.MongoClient(CONNECTION_STRING)

mydatabase = client['ishu_example'] 
mycollection=mydatabase['ishu_example_2'] 

result = mycollection.aggregate([
    {"$match": {"size": "medium"}},
    {"$group": {"_id": "$name", "totalQuantity": {"$sum": "$_id"}}}, 
    {"$skip": 2 },

])

# result = mycollection.aggregate([
#     {"$match": { "$and": [ {"size": "medium"}, {"price": 20} ] }},

# ])
for i in result:
    print(i)












#########################################################################

# import pymongo

# CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
# client = pymongo.MongoClient(CONNECTION_STRING)

# mydatabase = client['ishu_example'] 
# mycollection=mydatabase['ishu_example_2'] 

# result = mycollection.aggregate([
#     {"$match": {"size": "medium"}},
#     #{"$group": {"_id": "$name"}},
#     {"$group": {"_id": "$name", "totalQuantity": {"$sum": "$_id"}}},    #I've used the $first operator to get the price value for each name group.
#     {" $skip": 1 },
#     #{"$addFields": {"avgGrade": "ishu"}},
#    # {"$count": "medium"}  # it will direct provied the count 3 and no other output
# ])



# for i in result:
#     print(i)


# mycollection.insert_many( [
#    { "_id": 0, "name": "Pepperoni", "size": "small", "price": 19, "quantity": 10, "date": ( "2021-03-13T08:14:30Z" ) },
#    { "_id": 1, "name": "Pepperoni", "size": "medium", "price": 20,  "quantity": 20, "date" : ( "2021-03-13T09:13:24Z" ) },
#    { "_id": 2, "name": "Pepperoni", "size": "large", "price": 21, "quantity": 30, "date" : ( "2021-03-17T09:22:12Z" ) },
#    { "_id": 3, "name": "Cheese", "size": "small", "price": 12, "quantity": 15, "date" : ( "2021-03-13T11:21:39.736Z" ) },
#    { "_id": 4, "name": "Cheese", "size": "medium", "price": 13, "quantity":50, "date" : ( "2022-01-12T21:23:13.331Z" ) },
#    { "_id": 5, "name": "Cheese", "size": "large", "price": 14, "quantity": 10, "date" : ( "2022-01-12T05:08:13Z" ) },
#    { "_id": 6, "name": "Vegan", "size": "small", "price": 17,"quantity": 10, "date" : ( "2021-01-13T05:08:13Z" ) },
#    { "_id": 7, "name": "Vegan", "size": "medium", "price": 18, "quantity": 10, "date" : ( "2021-01-13T05:10:13Z" ) }
# ] )


