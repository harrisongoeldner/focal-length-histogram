# Import Modules
import sys, os
import tkinter as tk
from tkinter.filedialog import askdirectory
try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except:
    os.system('pip3 install Pillow')

# List files
def getfiles():
    tk.Tk().withdraw()
    directory = askdirectory()
    filelist=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if(file.lower().endswith(".jpg")):
                filelist.append(os.path.join(directory,file))
        for name in filelist:
            print(name) 
    return(filelist)

def exif(imagepath):
    exifdata=[]
    lens=''
    focal_length=''
    for (k,v) in Image.open(imagepath)._getexif().items():
            #print('%s = %s' % (TAGS.get(k), v))
            exifdata.append([TAGS.get(k),v])
            #print(dataset)
    for t in exifdata:
        if t[0] == "LensModel":
            lens = t[1]
        if t[0] == "FocalLength":
            focal_length = t[1]
    return lens, focal_length

def main():
    # Setup EXIF database
    exif_database = []
    for image in getfiles():
        func_data = exif(image)
        exif_database.append([func_data[0],func_data[1],image])
    print(exif_database)

if __name__ == "__main__":
    main()