import os
import urllib.request as request
import zipfile
from CNNClassifier import logger
from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

data_zip_path="artifacts/data_ingestion/data.zip"

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers= request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following information:\n {headers}")

        else:
            logger.info(f" File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str 
        Extracts the zip file into the data directory
        return: None 
        """
        unzip_path= self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(data_zip_path,'r') as zip_ref:
            zip_ref.extractall(unzip_path)