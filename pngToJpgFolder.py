# Converts PNG images to JPG

import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("Select images folder")
folder = filedialog.askdirectory() + "/"
folderJpg=folder + "/jpg/"

if not os.path.exists(folderJpg):
   os.mkdir(folderJpg)

with os.scandir(folder) as entries:
    i=0
    for entry in entries:
        i+=1
        fileStr = entry.name.removesuffix('.png')
        im = Image.open(folder + entry.name)
        rgb_im = im.convert('RGB')
        rgb_im.save(folderJpg + fileStr + '.jpg')

    print("Se han convertido " + i +" ficheros")    