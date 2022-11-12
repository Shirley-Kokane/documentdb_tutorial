import os
import sys
import pymongo
import json

#Insert sample data
# SEED_DATA = [{"time": "2022-07-24T19:06:49", "_id" : 118976, "movie" : "raiders+of+the+lost+ark", "year": 1986},
# { "time":"2022-07-24T21:06:14","_id" : 141755, "movie" : "what+ever+happened+to+baby+jane", "year": 1962},
# { "time":"2022-07-24T23:56:32","_id" : 199, "movie" : "that+thing+you+do", "year": 1996},
# { "time":"2022-07-25T02:11:27","_id" : 111053, "movie" : "irreversible", "year": 2002},
# { "time":"2022-07-26T08:58:44","_id" : 114450, "movie" : "antz", "year": 1998},
# { "time":"2022-07-26T14:57:01","_id" : 95456, "movie" : "braveheart", "year": 1995},
# { "time":"2022-07-26T19:39:44","_id" : 118971, "movie" : "pulp+fiction", "year": 1994},
# { "time":"2022-07-28T16:11:13","_id" : 46870, "movie" : "grumpier+old+men", "year": 1995},
# ]

#Insert sample data
with open("movie.json") as outfile:
    SEED_DATA = json.load(outfile)

#Get Amazon DocumentDB ceredentials from environment variables
username = os.environ.get("docbUser")
password = os.environ.get("docdbPass")
clusterendpoint = os.environ.get("docdbEndpoint")

#print('check',SEED_DATA[0])
def main():
    #Establish DocumentDB connection
    client = pymongo.MongoClient("mongodb://dbt:stormborn@docdb-2022-11-07-22-40-56.cluster-cbya07tevozy.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")#(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='rds-combined-ca-bundle.pem',retryWrites='false')
    #print(client.list_databases())
    try:
        dbt = client.get_database()
    except pymongo.errors.ConfigurationError:
        dbt = client.get_database('test')
    #dbt = client.get_database()#.profiles#sample_database
    print(dbt.name)
    profiles = dbt.profiles#.collection#['collection']
    print(profiles.find_one())

    #Insert data
    for seed in SEED_DATA[50:100]:
        profiles.insert_one(seed)
    print("Successfully inserted data")

    #Find a document
    query = {'_id': 199}
    print("Printing query results")
    print(profiles.find_one(query))

    #Update a document
    print("Updating document")
    #profiles.update_one(query, {'$set': {'movie': 'godfather'}})
    print(profiles.find_one(query))

    #Clean up
    #db.drop_collection('profiles')
    client.close()

if __name__ == '__main__':
    main()
