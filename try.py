def collectFirstTouchInfos():
    import platform,socket,json,re,uuid,psutil,os
    try:
        info={}
        info['platform-name']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['platform-architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['username']=os.environ.get('USERNAME')
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0**3)))+" GB"
        info['infection_date'] = 1123
        return json.dumps(info)
    except Exception as e:
        return "Problem Has Been Occured When Information Gathering"

print(collectFirstTouchInfos())


# {"platform-name": "Windows", "platform-release": "10", "platform-version": "10.0.19041", "platform-architecture": "AMD64", "hostname": "Kuheylan", "username": "Okan", "ip-address": "192.168.3.1", "mac-address": "dd:ff:df:dd:dd:ff", "processor": "Intel64 Family 6 Model 94 Stepping 3, GenuineIntel", "ram": "16 GB", "infection_date": 1123}