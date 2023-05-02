import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    users=pd.read_csv('users.csv')
    return users


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    users=read_data_from_csv()

    #Remove Unwanted columns
    def remove_unwanted_columns(users):
    # drop unwanted columns except for the allowed ones
        columns_to_drop = ['private/public', 'post count', 'Verified status']
        users.drop(columns=columns_to_drop, inplace=True)
    #columns_to_keep = ['id', 'comment', 'User  id', 'Photo id', 'created Timestamp']
    #comments = comments[columns_to_keep]
        return users
    #call remove_unwanted_columns() function to get dataframe
    users=remove_unwanted_columns(users)
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	username
    # 3.	created_at
    users.rename(columns={'name': 'username', 'created time': 'created_at'}, inplace=True)
    #export cleaned Dataset to newcsv file named "users_cleaned.csv"
    users.to_csv('users_cleaned.csv')
    return users


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()
