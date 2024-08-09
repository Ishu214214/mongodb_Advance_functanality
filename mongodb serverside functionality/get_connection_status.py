from flask import Flask  ,jsonify
import pymongo
import json


CONNECTION_STRING  = "mongodb+srv://atlasadmin:KGmYNHHfhvT59bxa@onesearch.k95bo.mongodb.net"
client = pymongo.MongoClient(CONNECTION_STRING)

mydatabase = client['ubuy_onesearch_v1']

connections_dict = mydatabase.command("serverStatus")["connections"]
print(connections_dict)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     connections_dict = mydatabase.command("serverStatus")["connections"]
#     print(connections_dict)

#     return jsonify(connections_dict)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)



