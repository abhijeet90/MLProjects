import os
import sys # To use our custome exception
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# In data injestion component any input that is required, we will give through this config

@dataclass
class DataInjestionConfig:
    train_data_path: str=os.path.join("artifact","train.csv")
    # Output will be stored in artifact folder
    # the file name is train.csv
    
    test_data_path: str =os.path.join("artifact","test.csv")
    raw_data_path: str =os.path.join("artifact","raw.csv")
    
    #above are the inputs that we are giving to data injestion component and data injestion component
    #knows where to save the train path, test path and data path
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataInjestionConfig()
    
    # If your data is stored in databases we will write code here
    def initiate_data_ingestion(self):
        logging.info("Entered the data injestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            
            train_set, test_set =train_test_split(df,test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            
            # The return info is required for data transformation
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,                                
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    
    
    
    
    
    
    
    
    
    
    
    
    
    