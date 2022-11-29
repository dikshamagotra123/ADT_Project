check_datatypes_text = "Checking the columns using suitable datatypes and replace animes where the number of episodes are unknown into nan and then convert everything to float"

sum_null_text = "How many missing values do we have for each column?"

remove_tv_text = "Removing rows where the film is not classified as 'TV'"

info_text = "It seems we still have 10 rows with missing genre values and also 116 rows with missing rating values. For the content based filtering, the genre of the show will be required so when it is time to develop the content based filtering model I will be dropping those 10 rows with missing genre values. On the other hand, with the collaborative filtering system, I am not required to used the genre values at all so I will simply use the whole dataset without the genre column."

rating_df_text = "Load ratings dataset"

replace_dt_text = "Instead of using -1, we will replace all ratings of -1 with a null value."

count_txt = "Count of Data"

success_text = "Cleaned Data files uploaded successfully"

cleaned_anime_text = "Read in the cleaned anime dataset"

drop_col_text = "Drop columns that will not be needed"

drop_na_text = "Drop rows where there are empty values in the genre column"

inconsistent_text = "the list of genres that a row contains was inconsistently formatted with some rows having ", " as a delimiter and others ",""

hot_encode_text = "Using scikit learn's MLB package to one hot encode the genres"

cleaned_rating_text = "Read in the cleaned rating dataset"

missing_text = "Remove missing values from the data"

sum_text = "How many missing values do we have?"

random_text = "Use the random library to generate a random user id"

drop_text = "Drop the columns that are not needed"

relevant_anime = "After that, we find the relevant animes and their genre information from the anime dataset."

sort_text = "Sort the genre animes by the anime_id's so that the rows correspond to the same anime in the user's rated dataframe"

drop_col_two_text = "Drop anime id and name columns"

rating_text = "With content based filtering, we create a matrix of the genres that the user watches. We then create weights for each genre where the higher the weight, the more likely the user enjoys that genre. To do this, we use the dot product between a matrix and a vector: the genre matrix and the ratings of each of the animes they watched (vector)."

tranpose_text = "Dot product"

weight_text = "These are the weights or in other words, the genre preferences, of random user. We can then use these weights to recommend animes to the user. First let's grab the full anime dataset with the genres hot one encoded. We then set the anime id as the index and remove the name column which will not be needed."

weighted_avg_text = "After this, we multiply the genres in the matrix with the weights and then divide it by the sum of the weights for a weighted average of the animes. This will mean the resulting values will be based on the user's weights and the genre(s) an anime is categorised as."

sort_weight_text = "The last step before we can finally recommend our user anime shows is to sort the values in descending order so we get the animes that would most appeal to the user at the top."

final_text = "After all that work creating the recommendation system, we now have the top 10 recommendations for this user "

rm_text = "Dropped the coloums which were not necessary for better memory optimization"

rm_na_tetxt = "Removed NA values"

surprie_text = "Using reader() we parse the file containing ratings and then loading dataFrame into model's dataset"

pred_rating_text = "estimated rating that the user '4271' will give on anime ID:'7088' "

dump_text = "exporting the recommendation system into a Pickle file for potentially usage in the future."