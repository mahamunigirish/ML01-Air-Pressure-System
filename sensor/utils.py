import pandas as pd 
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    This function  return collection as  dataframe 
    database_name: database name 
    collection_name : collection name 

    return pandas dataframe of a collection 
    """
    try:
        logging.info("Reading data from database : {database_name} and collction : {collection_name}")
        df= pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns",{df.columns})
        if "_id" in df.columns:
            logging.info(f"Droppoing column: _id")
            df =  df.drop("_id",axis=1)
            logging.info(f"rows and columns in df :{df.shape}")
            return df 
    except Exception as e:
        raise SensorException(e,sys)

