from PIL import Image

def get_exif(path):
    return Image.open(path).info

get_exif("/Users/harrisongoeldner/OneDrive/Pictures/Olympus/2020/2020-02-15/P2130004.JPG")