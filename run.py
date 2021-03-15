#script to read descriptions and add it to a json file along with it's deatils.

#!/usr/bin/env python3
import os, sys
import json
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

files = os.listdir(path)

for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r') as f:
      fruit_name = os.path.splitext(file)[0] #get the image name
      data = f.read()
      data = data.split("\n")
      #The data model in the Django application fruit has the following fields: name, weight, description and image_name
      fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
      response = requests.post(url, json=fruit_dic)
      response.raise_for_status()
      print(response.request.url)
      print(response.status_code)