#!/usr/bin/env python3
from PIL import Image
import os, sys

path = "supplier-data/images/"
pictures = os.listdir(path)
#pictures has all the image files.

for pic in pictures:
  #iterating through them
  if 'tiff' in pic:
    file_name = os.path.splitext(pic)[0] #split the name and extension
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    try:
      Image.open(path + pic).convert("RGB").resize((600,400)).save(outfile,"JPEG")
    except IOError:
      print("cannot convert", pic) #using try to avoid errors
