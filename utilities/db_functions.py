def download_anime_database():
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('CooperUnion/anime-recommendations-database','anime.csv','archive/')
    import_data_to_mongo(db_name="anime_db",collection_name="anime")
    return None

def download_rating_database():
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('CooperUnion/anime-recommendations-database','rating.csv')
    import_data_to_mongo(db_name="anime_db",collection_name="rating")
    return None

def import_data_to_mongo(db_name,collection_name):
    import csv
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[db_name]
    mycol = mydb[collection_name]

    #CSV to JSON Conversion
    csvfile = open(f"archive/{collection_name}.csv", 'r')
    reader = csv.DictReader( csvfile )
    if collection_name == "anime":
        header= ["anime_id", "name", "genre", "type", "episodes", "rating", "members"]
    else:
        header ["user_id","anime_id","rating"]

    for each in reader:
        row={}
        for field in header:
            if each[field] == '':
                row[field]=None
            else:
                row[field]=each[field]
        # print(row)
        mycol.insert_one(row)
    return "DATABASE IMPORTED"

def import_mongodb_to_dataframe(collection_name):
    import pymongo
    import pandas as pd
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["anime_db"]
    collection = mydb[collection_name]
    df = pd.DataFrame(list(collection.find({},{"_id":False})))
    return df

