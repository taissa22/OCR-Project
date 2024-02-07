from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import os
import json 
import pickle

assume_straight_pages=False
assume_straight_boxes=False

model = ocr_predictor(pretrained=True)
for i in range(50, 51):
    img = DocumentFile.from_images("new_images/im" + str(i) + ".jpg")
    result = model(img)
    result_json = result.export()
    #f = open(f"new_results/im{i}-text.json","w")
    #f.write(str(result_json))
    with open(f"new_results/json/im{i}-text.json", 'wb') as f:
        pickle.dump(result_json, f)
    #result.show()

