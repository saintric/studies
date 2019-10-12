#!usr/bin/env python3
import webbrowser
import os

os.chdir('C:your PATH here')

#url1 = "https://hangouts.google.com/?authuser=1"
#url2 = "https://www.messenger.com/login.php?"
#url3 = "https://twitter.com/home"
#url = "https://www.google.com/"
#
#webbrowser.open(url1)
#webbrowser.open(url2)
#webbrowser.open(url3)
#webbrowser.open(url)

#urls = "test.urls.txt"
#for url in urls:
#    print (url)

# lists of all url
file = open('test_urls.txt', 'r', encoding="ANSI") 
urls = file.readlines()
for url in urls:
#    print (url)
    webbrowser.open(url)

#def startupurls(url):
#    webbrowser.open(url)
#
#
#if __name__ == "__main__":
#    p = Pool(processes=5)
#    result = p.map(checkurl, urls)
#
#print("done in : ", time.time()-start)
