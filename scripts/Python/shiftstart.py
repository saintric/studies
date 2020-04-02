#! /usr/bin/env python3
# This setup the applications for shift start

import os
import time
import webbrowser

# delete Internet Explorer in User Pinned
pinnedTab = br'C:\Users\user\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar\Internet Explorer.lnk'
try:
    os.unlink(pinnedTab)
except OSError:
    pass

# opens Default App window
cmd = 'control /name Microsoft.DefaultPrograms /page pageDefaultProgram'
os.system(cmd)

# opens work App separately
os.chdir(br'C:\Users\user\Desktop\MyScripts')
with open('app.txt') as f:
    apps = f.read().splitlines()
for app in apps:
    os.startfile(app, 'open')

time.sleep(10) #wait for 10 seconds

# Opens favorite url to start shift
# lists of all url
with open('urls.txt') as f2:
    urls = f2.read().splitlines()
for url in urls:
    webbrowser.open(url)
