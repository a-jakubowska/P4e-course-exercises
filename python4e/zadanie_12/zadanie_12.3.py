import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter:')
iter=range(7)
for i in iter:
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")

    tags = soup('a')
    url=tags[17].get('href',None)
    print(url)

#html2=urllib.request.urlopen(link, context=ctx).read()
#soup2=BeautifulSoup(html2,"html.parser")
#print(soup2)

#tags2 = soup2('a')
#link2=tags2[2].get('href',None)
#print(link2)


#web = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
#for line in web:
    #print(line.decode().strip())

