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
    testdataFrame.drop("genre", axis=1, inplace=True)
    print("Here 3")
    return testdataFrame

def drop_na_values(dataFrame):
    dataFrame.dropna(inplace=True)
    return None

def sum_null_values(dataFrame):
    import pandas as pd
    import streamlit as st
    null_val = pd.isnull(dataFrame).sum()
    st.table(null_val.astype(str))
    return None