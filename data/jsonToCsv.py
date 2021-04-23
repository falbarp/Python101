import pandas as pd
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

filename=""

def openFile():
    Tk().withdraw() 
    filename = askopenfilename()
    print(filename)
    return filename

name= openFile()
df = pd.read_json (name)
export_csv = df.to_csv (r'./fromJson.csv', index = None, header=True)
