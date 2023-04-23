from pymongo import MongoClient

def asking_people(mangocluster):
    client = MongoClient(mangocluster,connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)
    db = client.bus
    data_in = db.bussituation
    results = data_in.find().sort('timestamp',-1).limit(1)
    print(db)
    print(data_in)
    qty = []
    
    for result in results:
        qty.append(result)
        

    return qty
