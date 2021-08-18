
import sys, os
from tkinter import Tk
from PIL import Image
from PIL.ExifTags import TAGS

#from tkinter.filedialog import askopenfilename
#imagename = askopenfilename()

imagename = "/Users/harrisongoeldner/OneDrive/Pictures/Olympus/2020/2020-02-15/P2130004.JPG"

image = Image.open(imagename)

exifdata = image.getexif()

for tagid in exifdata:
    tagname = TAGS.get(tagid, tagid)
    data = exifdata.get(tagid)
#    if isinstance(data, bytes):
#        data = data.decode()
    print(f"{tagname:25}: {data}")
