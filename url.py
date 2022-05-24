#to find different part of url
#take any url
import urllib.parse
url='https://ww55.affinity.net/sssdomweb?enk=f37b53b13385227d01e94cc4e0c83a31916e0b70db2cd6e5951b103acbf5f1a7ef2c530cc0fe75dcee32f77628e1480a3acec33b49c3549d297065f2975465e8f2c8d29d83cedfdb'
tpl=urllib.parse.urlparse(url)
print(tpl)  #to display the content of the tuple
 
 #to display different part of the url
print("Scheme",tpl.scheme)
print("Netloc",tpl.netloc)
print("path",tpl.path)
print("params",tpl.params)
print("port",tpl.port)
print("Total url",tpl.geturl)
