import pandas as pd
from surprise import SVD
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import GridSearchCV
from surprise.dump import dump

def rm_info(dataFrame):
    anime_df = pd.read_csv("datasets/cleaned_anime.csv")
    dataFrame = anime_df.loc[:, ["anime_id", "name", "rating"]]
    return(dataFrame)

def load_data(dataFrame):
    dataFrame = pd.read_csv("datasets/cleaned_rating.csv")
    return(dataFrame)

def drop_na_col(dataFrame):
    #removing the missing value
    dataFrame.dropna(inplace=True)
    # How many missing values do we have?
    return(dataFrame)

def load_df_surprise(dataFrame):
    # reader parses the file containing the ratings
    #Our rating scale is from 1 to 10 inclusive
    reader = Reader(rating_scale=(1, 10))

    # Load the dataframe into the model's dataset
    data = Dataset.load_from_df(dataFrame[["user_id", "anime_id", "rating"]], reader)
    return(data)

def pred_data(data):
    # Create parameters combinations
    params = {
    "n_epochs": [10, 15], "lr_all": [0.003, 0.005, 0.007], "reg_all": [0.01, 0.02, 0.03]
    }

    # Run the grid search using SVD and the parameters to find the best parameters for Root Mean Square Error and Mean Absolute Error
    gs = GridSearchCV(SVD, params, measures=['rmse', 'mae'], cv=3, joblib_verbose=2, n_jobs=-2)
    gs.fit(data)

    #algo for recommendation
    algo = gs.best_estimator["rsme"]
    algo.fit(data.build_full_trainset())
    # Just testing out the prediction method on user 4271 on anime id 7088
    pred = algo.predict(4271,7088).est
    dump("recommender.pkl", algo)
    return(pred)


    









