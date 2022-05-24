from pkgutil import ImpImporter


import urllib.request
file=urllib.request.urlopen("https://www.bing.com/news/search?q=Instagram&qpvt=instagram&FORM=EWRE")
print(file.read())
