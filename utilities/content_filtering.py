def drop_columns(dataFrame):
    # We will drop columns that will not be needed
    dataFrame.drop(["type", "episodes","rating", "members"], axis=1, inplace=True)
    return dataFrame

def drop_na_columns(dataFrame):
    dataFrame.dropna(subset=["genre"], inplace=True)
    return None

def set_delimeter(dataFrame):
    # I found that the list of genres that a row contains was inconsistently formatted with some rows having ", " as a delimiter and others ","
    dataFrame["genre"] = dataFrame["genre"].str.replace(", ", ",")
    # Then convert the genre column into a list so you can hot one encode the genres.
    dataFrame["genre"] = dataFrame["genre"].str.split(",")
    return dataFrame

def hot_encode_dataframe(dataFrame):
    import pandas as pd
    # Using scikit learn's MLB package to one hot encode the genres
    from sklearn.preprocessing import MultiLabelBinarizer

    # Code from https://stackoverflow.com/questions/45312377/how-to-one-hot-encode-from-a-pandas-column-containing-a-list
    mlb = MultiLabelBinarizer(sparse_output=True)

    
    testdataFrame = dataFrame.join(pd.DataFrame.sparse.from_spmatrix(
                    mlb.fit_transform(dataFrame["genre"]),
                    index=dataFrame.index,
                    columns=mlb.classes_))


    # Drop the origininal genre column
    testdataFrame.drop("genre", axis=1, inplace=True)
    return testdataFrame

def generate_random_user(dataFrame):
    # Use the random library to generate a random user id
    import random
    sys_random = random.SystemRandom()

    random_user_list = [64237,1,32768,6,8,632239,10,13,22,36,1204]
    # Pick a random id from the ratings dataset
    user = sys_random.choice(random_user_list)
    return user

def get_user_df(dataFrame,user_id):
    user_df = dataFrame[dataFrame["user_id"]==user_id]

    # Reset the indexes
    user_df.reset_index(drop=True, inplace=True)
    # Drop the columns that are not needed
    user_df = user_df.drop("user_id", axis=1)
    return user_df

def get_anime_in_user_df(anime_df,user_df):
    user_genre_df = anime_df[anime_df["anime_id"].isin(user_df["anime_id"])]
    return user_genre_df

def sort_anime_id(dataFrame):
    user_genre_df = dataFrame.sort_values("anime_id")
    user_genre_df.reset_index(drop=True, inplace=True)
    return user_genre_df

# Delete this function when random works
def drop_orphan_anime(dataFrame):
    dataFrame.drop([0, 1], axis=0, inplace=True)
    dataFrame.reset_index(drop=True, inplace=True)
    return dataFrame

def user_genre_matrix(dataFrame):
    dataFrame = dataFrame.drop(["anime_id", "name"], axis=1)
    return dataFrame

def user_rating(dataFrame):
    return dataFrame["rating"]

def dot_product(user_genre_matrix,user_rating):
    weights = user_genre_matrix.transpose().dot(user_rating)
    return weights

def set_index(dataFrame):
    recommendation_table = dataFrame.set_index("anime_id")
    # Drop the name column
    recommendation_table.drop("name", axis=1, inplace=True)
    return recommendation_table

def get_weighted_avg(recommendation_table, weights):
    recommendation_series = (recommendation_table * weights).sum(axis=1) / weights.sum()
    return recommendation_series

def sort_desc_fun(recommendation_series):
    recommendations = recommendation_series.sort_values(ascending=False)
    return recommendations

def top_10_recc(anime_df, recommendations):
    recommendations_df = anime_df.loc[anime_df["anime_id"].isin(recommendations.head(10).keys())]
    # Set the index of the dataframe to the anime ids
    recommendations_df.set_index("anime_id", inplace=True)
    # Use loc and the anime ids of the top 10 anime recommendations to preserve the order and output that to the user
    final_df = recommendations_df.loc[recommendations.head(10).keys()][["name"]]
    return final_df
