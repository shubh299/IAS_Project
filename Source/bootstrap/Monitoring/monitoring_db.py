import pymongo

client=pymongo.MongoClient(" mongo server address here")

db = client['app_manager']

#pass component name and status
def update_component_status(component_name,status):
    db.component_status.update_one({"component_name":component_name},{"$set":{"status":status}},upsert=True)
    return None
