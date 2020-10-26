import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import main

if main.isInTargetFiles("txt") and not main.isInTargetFiles("okan"):
    print("Binary Search TEST IS COMPLETED SUCCESSFULLY")
else:
    print("Binary Search TEST IS FAILED!")

if main.isValidFile("test.txt") and not main.isValidFile("test.okan"):
    print("Valid File TEST IS COMPLETED SUCCESSFULLY")
else:
    print("Valid File TEST IS FAILED!")