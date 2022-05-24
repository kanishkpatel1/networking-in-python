import urllib.request
try:
    file=urllib.request.urlopen("https://www.bing.com/news/search?q=Instagram&qpvt=instagram&FORM=EWRE")
    content=file.read()
except urllib.error.HTTPError:
    print("The web page does not exist:")
f=open('myfile.html','wb')
f.write(content)
f.close()

