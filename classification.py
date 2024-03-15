"""This module contains the ImageClassification class, which is responsible for classifying images using a pre-trained ResNet-50 model and saving the results to a CSV file."""

import csv
import os

import tkinter
import torch

from PIL import Image
from tkinter import messagebox
from tkinter import filedialog
from torchvision import transforms
from torchvision.models import resnet50
from torchvision.models.resnet import ResNet50_Weights as weights


class ImageClassification:
    """Classify images using a pre-trained ResNet-50 model and save the results to a CSV file."""

    def __init__(self):
        """
        Constructs an ImageClassification object.

        Args:
            weights: The weights to be used by the ResNet-50 model. Defaults to the pre-trained weights.
            model: The model used was resnet50, which is a 50-layer deep neural network that allows distinguishing different classes of animals and has the ability to learn complex representations, it is also very efficient in training and pre-training on large data sets.
            transform: The image transformation to be applied to the input images.
                transforms.compose: The transformation pipeline to be applied to the input images.
                transforms.resize: Resize the input images to 224x224 pixels.
                transforms.centercrop: Crop the input images to 224x224 pixels.
                transforms.totensor: Convert the input images to PyTorch tensors.
                transforms.normalize: Normalize the input images using the mean and standard deviation of the ImageNet dataset.
        """
        self.weights = weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()
        self.transform = transforms.Compose(
            [
                transforms.Resize(224),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    def select_directory(self):
        """
        Select a directory containing the images to be classified.

        Args:
            root_window: The root window of the file dialog.
            directory: The path to the selected directory.

        Returns:
            The path to the selected directory.

        """
        root_window = tkinter.Tk()
        root_window.withdraw()
        directory = filedialog.askdirectory(
            title="Select the directory containing the images"
        )
        return directory

    def get_files_names(self, selected_directory: str):
        """
        Get the names of the files in the selected directory.

        Args:
            selected_directory (str): The path to the selected directory.

        Returns:
            str: The names of the files in the selected directory.
        """
        return os.listdir(selected_directory)

    def classify_and_save_results(self, selected_directory: str, filenames: str):
        """
        Converts the input images to PyTorch tensors, classifies them using the ResNet-50 model, and saves the results to a CSV file.

        Args:
            selected_directory (str): The path to the selected directory.
            filenames (str): The names of the files in the selected directory.
        """
        output = []
        for filename in filenames:
            if filename.endswith((".jpg", ".png", ".jpeg")):
                image_path = os.path.join(selected_directory, filename)
                classification = self.classify_image(image_path)
                output.append([filename, classification])
        self.export_to_csv(output)
        messagebox.showinfo(
            "Classification Complete",
            "Classification of images saved in 'resultados.csv'",
        )
        os.system("resultados.csv")

    def classify_image(self, image_path: str):
        """Classify the input image using the ResNet-50 model.

        Args:
            image_path (str): path to the image to be classified.
            animal range(0, 397): The range of the animal categories in the ImageNet dataset.

        Returns:
            str: The classification result for the input image, return None if the image is not an animal and return Name of the classification if it is an animal.
        """
        image = Image.open(image_path)
        image = self.transform(image).unsqueeze(0)

        with torch.no_grad():
            output = self.model(image)

        _, predicted = torch.max(output, 1)
        class_index = predicted.item()
        Name = self.weights.meta["categories"][int(class_index)]

        animal = range(0, 397)
        if class_index in animal:
            return Name
        else:
            return "None"

    def export_to_csv(self, output: str):
        """
        Save the classification results to a CSV file.

        Args:
            output (str): The name of the file to save the classification results to.

        Performs the following steps:
            1. Open the file 'resultados.csv' for writing.
            2. Create a CSV writer object.
            3. Write the header row to the CSV file.
            4. Write the classification results to the CSV file.
            5. Close the file 'resultados.csv'.

        Raises: ValueError: If the file 'resultados.csv' is already open.
        """
        try:
            with open("resultados.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Image Name", " Classification Result"])
                writer.writerows(output)
        except PermissionError:
            messagebox.showerror(
                "Permission Denied",
                "The file 'resultados.csv' is already open. Please close it and try again.",
            )
            raise
        except Exception as e:
            messagebox.showerror(
                "An Error Occurred",
                f"An error occurred while saving the classification results to 'resultados.csv': {e}",
            )
