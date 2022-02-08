from shutil import move
from utils.config import config

import os

def preprocess_singlefile(file_path:str, out_folder:str)->str:
    os.makedirs(out_folder, exist_ok = True)
    return move(file_path, file_path.replace(config["DOCKER_INPUT_FOLDER"], out_folder).replace('.nii.gz', '_0000.nii.gz'))
