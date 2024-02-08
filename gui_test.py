import tkinter as tk
from tkinter import ttk
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import matplotlib.pyplot as plt

assume_straight_pages=False
assume_straight_boxes=False

model = ocr_predictor(pretrained=True)

def choose_img():
    if int(entryInt.get()) > 39:
        output_string.set('Only 13 images in the database')
    else:
        img = DocumentFile.from_images("images/test-" + str(entryInt.get()) + ".jpg")
        result = model(img)
        result.show()
        synthetic_pages = result.synthesize()
        plt.imshow(synthetic_pages[0]); plt.axis('off'); plt.show()
        output_string.set('')

window = tk.Tk()
window.title("Document OCR")
window.geometry("300x150")


#title
title_label = ttk.Label(master= window, text= 'DocTR test results', font= 'Arial 18')
title_label.pack()

#input img
input_frame = ttk.Frame(master= window)
entryInt = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable=entryInt)
button = ttk.Button(master= input_frame, text = 'Enter', command= choose_img)
button_close = ttk.Button(master= input_frame, text= 'Close', command= window.destroy)
entry.pack(side='left', padx=10)
button.pack(side='left')
button_close.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= 'Output', font='Arial 10', textvariable=output_string)
output_label.pack(pady=5)

#run
window.mainloop()