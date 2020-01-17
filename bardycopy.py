import wget
import datetime
from shutil import copyfile

###Destination###
dest = 'N:/someplace/someplace'

###Creds###
user = 'Bardy'
pw= 'DoNotPlebLord'


###Links without https://###
url = ['www.facebook.com', 'www.google.com', 'another']


for u in url:
    file = wget(f'https://{user}:{pw}@{u}')
    copyfile(file, dest)