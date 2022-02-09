# refactored-octo-chainsaw
# Neural Network-Based Segmentation of MS Lesions in FLAIR Images

This repository contains the inference engine of nnUnet based Multiple Sceloris segmentation in the FLAIR sequence. The model is trained on data of a variety of data and does a good segmentation.  The inference engine is dockerized in to allow for plug and play approach for segmentation of NifTi data.

<img width="637" alt="Example Screenshot" src="https://user-images.githubusercontent.com/23334003/153212469-78c8668c-3f5f-47c6-b2cd-dfd47cd423df.png">

----------------

# Neural Network-Based Segmentation of MS Lesions in FLAIR Images

This repository contains the inference engine of nnUnet based Multiple Sceloris segmentation in the FLAIR sequence. The model is trained on data of a variety of data and does a good segmentation.  The inference engine is dockerized in to allow for plug and play approach for segmentation of NifTi data.

----------------

### Easily segment your data with one command

Once all the docker and its dependencies are installed, you can simply test the ms lesion segmentation on your FLAIR NifTi data with:

**Run with GPUs:**

default:
```
docker run --gpus all --user "$(id -u):$(id -g)" -v <inpdir>:/mslesion_seg/inp -v <outdir>:/mslesion_seg/out aparida12/mslesion_seg
```

**Run without GPUs:**

default:
```
docker run --user "$(id -u):$(id -g)" -v <inpdir>:/mslesion_seg/inp -v <outdir>:/mslesion_seg/out aparida12/mslesion_seg
```
 
where:
- `<inpdir>` is the directory with all NifTi files(extn .nii.gz; .nii will be ignored) that need to be segmented.
- `<outdir>` is the directory where all outputs are stored(`<inpdir>` should not be `<outdir>`). 

----------------

### Run in a non docker setup
 - Install all requirements `pip install -r requirements.txt`
 - Paste all the trained weights/plans etc in the `./checkpoints` folder
 - edit the `config.yaml` accoring to the desire.
 - Run the segmentation by `python segment_lesion.py`

----------------
### Input Folder Structure

The input folder should follow a similar structure as shown below. Other files and folders may exist but will be ignored by the method.

```
│
└───<inpdir>
│   │   file011.nii.gz
│   │   file012.nii.gz
│   │   file012.nii.gz
│    |.

```
----------------
### Output Folder Structure

After processing is over the `<outdir>` has all the segmentation. The names of the segmented files are the same as the input files. 
```
│
└───<outdir>
│   │   file011.nii.gz
│   │   file012.nii.gz
│   │   file012.nii.gz
│    |.

```
----------------

###  External Links
 - [Code Repo](https://github.com/deepc-health/refactored-octo-chainsaw)
 - [Docker Repo](https://hub.docker.com/r/aparida12/mslesion_seg) 
--------------------------------
--------------------------------

Once all the docker and its dependencies are installed, you can simply test the ms lesion segmentation on your FLAIR NifTi data with:

**Run with GPUs:**

default:
```
docker run --gpus all --user "$(id -u):$(id -g)" -v <inpdir>:/mslesion_seg/inp -v <outdir>:/mslesion_seg/out aparida12/mslesion_seg
```

**Run without GPUs:**

default:
```
docker run --user "$(id -u):$(id -g)" -v <inpdir>:/mslesion_seg/inp -v <outdir>:/mslesion_seg/out aparida12/mslesion_seg
```
 
where:
- `<inpdir>` is the directory with all NifTi files(extn .nii.gz; .nii will be ignored) that need to be segmented.
- `<outdir>` is the directory where all outputs are stored(`<inpdir>` should not be `<outdir>`). 

----------------



### Input Folder Structure

The input folder should follow a similar structure as shown below. Other files and folders may exist but will be ignored by the method.

```
│
└───<inpdir>
│   │   file011.nii.gz
│   │   file012.nii.gz
│   │   file012.nii.gz
│    |.

```
----------------
### Output Folder Structure

After processing is over the `<outdir>` has all the segmentation. The names of the segmented files are the same as the input files. 
```
│
└───<outdir>
│   │   file011.nii.gz
│   │   file012.nii.gz
│   │   file012.nii.gz
│    |.

```
----------------

###  External Links
 - [Code Repo](https://github.com/deepc-health/refactored-octo-chainsaw)
 - [Docker Repo](https://github.com/deepc-health/refactored-octo-chainsaw) 
--------------------------------
--------------------------------
