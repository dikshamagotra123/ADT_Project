def download_database():
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('CooperUnion/anime-recommendations-database','anime.csv','archive/')
    # api.dataset_download_file('CooperUnion/anime-recommendations-database','rating.csv')
    import_data_to_mongo()

    return None

def import_data_to_mongo():
    import csv
    import pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["anime_db"]
    mycol = mydb["anime"]
    #CSV to JSON Conversion
    csvfile = open('archive/anime.csv', 'r')
    reader = csv.DictReader( csvfile )
    header= ["anime_id", "name", "genre", "type", "episodes", "rating", "members"]

    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]
        # print(row)
        mycol.insert_one(row)
    return "DATABASE IMPORTED"

def import_mongodb_to_dataframe():
    import pymongo
    import pandas as pd
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["anime_db"]
    collection = mydb["anime"]
    df = pd.DataFrame(list(collection.find({},{"_id":False})))
    return df

