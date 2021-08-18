import os
from tkinter.filedialog import askdirectory
import tkinter as tk

tk.Tk().withdraw()
directory = askdirectory()
filelist=[]

for root, dirs, files in os.walk(directory):
    for file in files:
        if(file.lower().endswith(".jpg")):
            filelist.append(os.path.join(directory,file))
for name in filelist:
    print(name)