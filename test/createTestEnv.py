import os
import sys
from random import randint
import shutil

# location of creating test env
path = os.path.join(os.path.expanduser('~'),"test")

deep = 1

content = {"txt":"human readable text Layer {}",
            "xml":"<apt> human readable text <al> Layer {} </al> </apt>",
            "html": "<html> <head> <title> APT-Al </title> </head> <body> human readable text Layer {} </body> </html>",
            "py": "print('human readable text Layer {}')",
            "fake": "dont touch me {}"}

def createLayer(path,remainLayer):
    global content
    os.mkdir(path)

    file_count = randint(0,6)
    

    for i in range(file_count):
        file_ext, file_content = list(content.items())[randint(0,len(content.keys())-1)]
        file_name = "file"+str(i)+"."+file_ext
        file_path = os.path.join(path,file_name)
        print(file_path)
        with open(file_path, "w") as newFile:
            print(file_content.format(remainLayer), file=newFile)
    
    if remainLayer:     
        directory_count = randint(0,3)
        for i in range(directory_count):
            dirname_path = os.path.join(path, "goDeep"+str(remainLayer-1)+"_"+str(i))
            createLayer(dirname_path,remainLayer-1)

def cleanTestLoc(path):   
    try:
        shutil.rmtree(path)
    except:
        os.mkdir(path)

cleanTestLoc(path)
createLayer(path,deep)