import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import starter

if starter.isInTargetFiles("txt") and not starter.isInTargetFiles("okan"):
    print("Binary Search TEST IS COMPLETED SUCCESSFULLY")
else:
    print("Binary Search TEST IS FAILED!")

if starter.isValidFile("test.txt") and not starter.isValidFile("test.okan"):
    print("Valid File TEST IS COMPLETED SUCCESSFULLY")
else:
    print("Valid File TEST IS FAILED!")