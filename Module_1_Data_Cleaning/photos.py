import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def read_data_from_csv():
    photos=pd.read_csv('photos.csv')
    return photos


def data_cleaning():
    #DO NOT REMOVE FOLLOWING LINE
    photos=read_data_from_csv()

    #Select only prefered columns
    photos=photos[['id', 'image link', 'user ID', 'created dat']]

    #rename columns, only these columns are allowed in the dataset
    # 1.	id
    # 2.	image_url
    # 3.	user_id
    # 4.	created_date
    photos.rename(columns={'image link': 'image_url', 'user ID': 'user_id', 
    'created dat': 'created_date'}, inplace=True)
    #export cleaned Dataset to newcsv file named "photos_cleaned.csv"
    photos.to_csv('photos_cleaned.csv')
    return photos


#Do not Delete the Following function
def task_runner():
    data_cleaning()

task_runner()
