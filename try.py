from postInfection import PostInfection
import utils

#pi = PostInfection(1,1,"online",utils.when_did_i_work,utils.rsa_public_key)
#print(pi.changeWallpaper())

import os
def whichFile():
    for filee in os.listdir():
        if filee[-utils._len_aesIV_file_store_name:] == utils.aesIV_file_store_name:
            return filee

print(whichFile())