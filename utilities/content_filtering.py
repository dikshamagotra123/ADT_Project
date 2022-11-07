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
    print("Here 1")
    
    testdataFrame = dataFrame.join(pd.DataFrame.sparse.from_spmatrix(
                    mlb.fit_transform(dataFrame["genre"]),
                    index=dataFrame.index,
                    columns=mlb.classes_))

    print("Here 2")
    # Drop the origininal genre column
    dataFrame.drop("genre", axis=1, inplace=True)
    return dataFrame

def generate_random_user(dataFrame):
    # Use the random library to generate a random user id
    import random
    # Set random seed (for reproducibility)
    random.seed(10)

    # Pick a random id from the ratings dataset
    user = random.randint(dataFrame["user_id"].min(), dataFrame["user_id"].max())
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

def drop_orphan_anime(dataFrame):
    dataFrame.drop([0, 1], axis=0, inplace=True)
    dataFrame.reset_index(drop=True, inplace=True)
    return dataFrame

def create_genre_matrix(dataFrame):
    dataFrame = dataFrame.drop(["anime_id", "name"], axis=1)

def user_rating(dataFrame):
    return dataFrame["rating"]

def dot_product(user_genre_matrix,user_rating):
    weights = user_genre_matrix.transpose().dot(user_rating["rating"])
    return weights

