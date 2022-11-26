check_datatypes_text = "Checking the columns using suitable datatypes and replace animes where the number of episodes are unknown into nan and then convert everything to float"

sum_null_text = "How many missing values do we have for each column?"

remove_tv_text = "Removing rows where the film is not classified as 'TV'"

info_text = "It seems we still have 10 rows with missing genre values and also 116 rows with missing rating values. For the content based filtering, the genre of the show will be required so when it is time to develop the content based filtering model I will be dropping those 10 rows with missing genre values. On the other hand, with the collaborative filtering system, I am not required to used the genre values at all so I will simply use the whole dataset without the genre column."

rating_df_text = "Load ratings dataset"

replace_dt_text = "Instead of using -1, we will replace all ratings of -1 with a null value."

count_txt = "Count of Data"

success_text = "Cleaned Data files uploaded successfully"