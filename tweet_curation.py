#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:49:45 2022

@author: felixrosenbergernew

There were several JSON syntax issues found in the dataset which this program aims to remove as part of the data curation.
"""

with open("10000 tweets 1.json", "r") as f:
    with open("tweets clean.json", "w") as out:
        out.write("[") # include opening bracket
        for line in f:
            if "/*" not in line and "NumberLong" not in line and "ObjectId" not in line:
                out.write(line) # only write lines back to file that do not show the upper patterns
        out.write("]") # include closing bracket
        
with open("tweets clean.json", "r+") as inp:
    text = inp.read()
    inp.seek(0)
    inp.write(text.replace("}\n\n{", "},\n{")) # place commas between JSON objects
    
with open("tweets clean.json", "r") as file:
    filedata = file.read()
    
filedata = filedata.replace("\"hashtags\" : []", "\"hashtags\" : [\n\t\t{\n\t\t\t\"text\" : \"NA\"\n\t\t}\n\t]") #replace empty hashtags with NA

with open("tweets_clean.json", "w") as file:
    file.write(filedata)

