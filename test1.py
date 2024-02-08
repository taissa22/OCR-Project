from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from torch import nn
import torch as torch
import os
import json 
import pickle
import matplotlib.pyplot as plt

def export_doc(result):
    with open(f"new_results/text-images/{i}-text.txt", 'w') as f:
        f.write(str(result))

def show_results(result):
    synthetic_pages = result.synthesize()
    plt.imshow(synthetic_pages[0]); plt.axis('off'); plt.show()

def create_json(result):
    result_json = result.export()
    with open(f"new_results/json_results/im{i}-text.json", 'w') as f:
        json.dump(result_json, f)
    
    
model = ocr_predictor(pretrained=True, assume_straight_pages=True)
for i in range(1, 51):
    img = DocumentFile.from_images("new_images/im" + str(i) + ".jpg")
    result = model(img)
    result.show()
    


