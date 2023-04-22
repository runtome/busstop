from pymongo import MongoClient

def asking_people(mangocluster):
    client = MongoClient(mangocluster)
    db = client.bus
    data_in = db.bussituation
    results = data_in.find().sort('timestamp',-1).limit(1)
    
    qty = []
    
    for result in results:
        qty.append(result)
        

    return qty
