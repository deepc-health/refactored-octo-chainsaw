from utils.preprocess import preprocess_singlefile
from utils.config import config
import multiprocessing 
import glob
import torch
from nnunet.inference.predict import  predict_from_folder

cpu_count = multiprocessing.cpu_count()

input_folder = config["DOCKER_INPUT_FOLDER"]
input_files = glob.glob(input_folder+'/*.nii.gz')
for file in input_files:
    print("Preprocessing file: " + file)
    preprocess_singlefile(file, config["PREPROCESS_FILE_FOLDER"])

input_files = glob.glob(config["PREPROCESS_FILE_FOLDER"]+'/*.nii.gz')
for file in input_files:
    print("Preprocessed file: " + file)


output_folder = config["DOCKER_OUTPUT_FOLDER"] 
model_folder = config["MODEL_FOLDER"]
use_gpu = True if torch.cuda.device_count()>0 else False

predict_from_folder(model_folder, config["PREPROCESS_FILE_FOLDER"], config["DOCKER_OUTPUT_FOLDER"], folds=[config["FOLD_NO"]], save_npz=False, num_threads_preprocessing=cpu_count,
                        num_threads_nifti_save=cpu_count, lowres_segmentations=None, part_id=0, num_parts=1, tta=False,
                        overwrite_existing=True, mode="normal", overwrite_all_in_gpu=use_gpu,
                        mixed_precision=True,
                        step_size=0.5, checkpoint_name=config["CHECKPOINT_NAME"], disable_postprocessing=True)
