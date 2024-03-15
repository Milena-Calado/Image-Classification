import csv  
import os   
import tkinter
from tkinter import messagebox  
from PIL import Image  
from tkinter import filedialog  
import torch  
from torchvision import transforms  
from torchvision.models import resnet50  
from torchvision.models.resnet import ResNet50_Weights 

class ImageClassification:
    def __init__(self):
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights) 
        self.model.eval() 
        self.transform = transforms.Compose([
            transforms.Resize(224),  
            transforms.CenterCrop(224),  
            transforms.ToTensor(),  
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  
        ])

    def select_directory(self):
        root_window = tkinter.Tk()  
        root_window.withdraw()  
        directory = filedialog.askdirectory(title="Select the directory containing the images") 
        return directory  

    def get_files_names(self, selected_directory):
        return os.listdir(selected_directory)  

    def classify_and_save_results(self, selected_directory, filenames):
        output = []  
        for filename in filenames:  
            if filename.endswith(('.jpg', '.png', '.jpeg')): 
                image_path = os.path.join(selected_directory, filename)  
                classification = self.classify_image(image_path)  
                output.append([filename,  classification])  
        self.export_to_csv(output)  
        messagebox.showinfo("Classification Complete", "Classification of images saved in 'resultados.csv'")        
        os.system('resultados.csv')

    def classify_image(self, image_path):
        img = Image.open(image_path)  
        img = self.transform(img).unsqueeze(0)  

        with torch.no_grad():  
            output = self.model(img)  

        _, predicted = torch.max(output, 1)  
        class_index = predicted.item() 
        Name=self.weights.meta['categories'][int(class_index)]
        
        animal = range(0, 397)  
        if class_index in animal:
            return Name
        else:
            return 'None'

    def export_to_csv(self, output):
        with open('resultados.csv', 'w', newline='') as file:  
            writer = csv.writer(file)  
            writer.writerow(["Image Name", " Classification Result"])  
            writer.writerows(output)
