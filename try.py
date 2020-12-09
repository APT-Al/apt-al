import os,sys

from shutil import copyfile


copyfile(sys.argv[0],"/root/"+sys.argv[0])