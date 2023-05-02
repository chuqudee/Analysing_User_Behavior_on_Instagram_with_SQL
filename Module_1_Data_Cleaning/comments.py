import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    comments=pd.read_csv('comments.csv')
    return comments

def remove_unwanted_columns(comments):
    # drop unwanted columns except for the allowed ones
    #columns_to_drop = ['posted date', 'emoji used', 'Hashtags used count']
    #comments.drop(columns=columns_to_drop, inplace=True)
    columns_to_keep = ['id', 'comment', 'User id', 'Photo id', 'created Timestamp']
    comments = comments[columns_to_keep]
    return comments
    
def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    #call remove_unwanted_columns() function to get dataframe
    comments=read_data_from_csv()
    #Remove Unwanted columns
    comments=remove_unwanted_columns(comments)
    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	comment_text
    # 3.	user_id
    # 4.	photo_id
    # 5.	created_at
    comments.rename(columns={'User id': 'user id', 'Photo id': 'photo_id',
                             'comment': 'comment_text', 
                             'created Timestamp': 'created_at'}, inplace=True)
    
    #export cleaned Dataset to newcsv file named "comments_cleaned.csv"
    comments.to_csv('comments_cleaned.csv', index=False)
    return comments


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()

