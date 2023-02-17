from pymongo import MongoClient
#client = MongoClient("mongodb://{user}:{password}@{host}:{port}")
client = MongoClient("mongodb://172.16.1.41:27017/management-records.managementrecords?replicaSet=haddacloud-rs&readPreference=secondaryPreferred", directConnection=False)
db = client.database
#db = client
try:
    db.command("serverStatus")
except Exception as e: 
    print(e)
else:
    print("You are connected!")
client.close()