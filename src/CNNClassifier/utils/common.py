import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from CNNClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """reads yaml file
    
    Args:path_to_yaml (str): path to yaml file
    
    Raises: 
     ValueError: if yaml file is empty
     e: empty file
     
    Returns:

     ConfigBox: configuration box 
     """
    try: 
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file{path_to_yaml}loaded Successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f"yaml file{path_to_yaml} is empty")
    except Exception as e:
        raise e    



@ensure_annotations
def create_directories(path_to_directories: list , verbose=True):
    """creates directories
    
    Args: 
        path_to_directories(list): list of path of directories
        
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'created directory at:{path}')


@ensure_annotations
def save_json(path:Path , data :dict):
    """
    saves json file

     Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open (path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved Successfully at {path}")

 
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """
    Loads json files data

     Args:
        path (Path): path to json file

     returns: 
        ConfigBox : data as class attribute instead of dict
    """
    with open (path) as f:
        content=json.load(f)

    logger.info(f"json file at {path} loaded successfully")
    return ConfigBox(content)

@ensure_annotations
def save_bin( data :Any, path:Path):

    """
    saves binary file

     Args:
        data (Any): data to be saved as binary file
        path (Path): path to binary  file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved Successfully at {path}")


@ensure_annotations
def load_bin(path:Path)->Any:

    """
    Loads binary file

     Args:
        path (Path): path to binary  file

     returns: 
        Any : object stored in file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path:Path)-> str:

    """
    get size in kb

     Args:
        path (Path): path of the file
    """
    size_in_kb= round(os.path.getsize(path)/1024)
    return f"{size_in_kb}kb"

def decodeImage(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImapePath):
    with open(croppedImapePath, "rb") as f:
        return base64.b64encode(f.read())