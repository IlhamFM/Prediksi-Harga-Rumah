import yaml
import joblib
import platform
import os
from pathlib import Path

def get_dir():
    return Path(os.getcwd())
    
def dir_parent():
    return str(get_dir().parent)

def get_platform():
    return platform.system()
    
def get_params():
    if get_platform() == "Windows":
       dir_params = "\\config\\params.yaml"
    else:
       dir_params = "config/params.yaml"
    return  dir_params

def load_params(lokasi_file):
    with open(lokasi_file, 'r') as file:
        params = yaml.safe_load(file)
        
    return params

def pickle_load(file_path: str):
    # Load and return pickle file
    return joblib.load(file_path)

def pickle_dump(data, file_path: str) -> None:
    # Dump data into file
    joblib.dump(data, file_path)
    
def cek_path_os(path):
    new_path = ""
    for p in path.split("/"):
        if get_platform() == "Windows":
            new_path = new_path + "\\" + p
        else:
            new_path = path
            break
    return new_path