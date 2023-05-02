import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    follows=pd.read_csv('follows.csv')
    return follows

def remove_unwanted_columns(follows):
    # drop unwanted columns except for the allowed ones
    columns_to_drop = ['is follower active', 'followee Acc status']
    follows.drop(columns=columns_to_drop, inplace=True)
    #columns_to_keep = ['id', 'comment', 'User  id', 'Photo id', 'created Timestamp']
    #comments = comments[columns_to_keep]
    return follows
    
def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    follows=read_data_from_csv()

    #Remove Unwanted columns
    follows=remove_unwanted_columns(follows)
    #rename columns, only these columns are allowed in the dataset
    # 1.	follower_id
    # 2.	followee_id
    # 3.	created_at
    follows.rename(columns={'follower': 'follower_id', 'followee ': 'followee_id',
                             'created time': 'created_at'}, inplace=True)
    #export cleaned Dataset to newcsv file named "follows_cleaned.csv"
    follows.to_csv('follows_cleaned.csv')
    return follows


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()
