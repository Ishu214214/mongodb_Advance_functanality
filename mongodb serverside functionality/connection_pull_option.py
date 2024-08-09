from pymongo import MongoClient
from queue import Queue
import time

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"

class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.connections = Queue(maxsize = max_connections)

    def get_connection(self):
        connection = None
        if not self.connections.full():
            connection = MongoClient(CONNECTION_STRING)
            self.connections.put(connection)
        return connection

    def release_connection(self, connection):
        connection.close()
        self.connections.get()


if __name__ == "__main__":
    pool = ConnectionPool( max_connections = 3 )
    while 1:
        client = pool.get_connection()
        if client:

            """     call the collection   """
            mydatabase = client['copy_last_id']
            mycollection = mydatabase['copy_ubuy_last_id1']

            connections_dict = mydatabase.command("serverStatus")["connections"]
            available = connections_dict['available']
            current = connections_dict['current']
            print(connections_dict)

            if current < 800:
                """     perform the task    """
                print(mycollection.find_one({"name": "Bob", "age": 25}))
            else:
                print(" we have reatch the mongodb connection ")
                print("sleep 120 sec")
                time.sleep(20)

        """     close the connection which we have read """
        pool.release_connection(client)
        
        print("sleep 20 sec")
        time.sleep(12)


"""
output is 
{'current': 103, 'available': 397, 'totalCreated': 4415}
 we have reatch the mongodb connection 
sleep 120 sec
{'current': 104, 'available': 396, 'totalCreated': 4418}
 we have reatch the mongodb connection 
sleep 120 sec

"""




