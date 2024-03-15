# Image Classification 

Image classification project, using the ResNet-50 pre-trained model to identify whether an image contains an animal.
According to the IMAGENET 1000 Class List (IMAGENET.md) attached to this repository, animal classes are in the range 0 to 397, so I used this range to refine the image classification.

## Project's goal

The objective of the project is for a user to select a directory containing images and these images to be classified as "Animal-Category" or "None", based on the model output.

## Requirements

- Make sure you have Python and pip or conda installed on your system.

- If you don't have Anaconda, access this tutorial on how to download and install Anaconda in Python:
```
https://www.anaconda.com/products/distribution
```

- Install the necessary dependencies:
```
pip install -r requirements.txt
``` 
- make sure you are in the conda environment (voxar), to create the environment, run the command:
```
conda env create -f .\environment.yml 
```
## Instructions for use

To use the image classifier, follow these steps:

1. Run the `main.py` script with the command:
   ```
   python main.py
   ```
2. A window will open and you must select the directory containing the images.
3. After selecting, wait until the sorting process is completed.
4. A message will be displayed informing you that the image classification has been completed.
5. The 'resultados.csv' file will be displayed on the screen.
