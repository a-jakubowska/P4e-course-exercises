 print('Lets start!')


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#url = input('Enter - ')
url='http://py4e-data.dr-chuck.net/comments_1451427.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


sum=list()
suma= int()
# Retrieve all of the anchor tags


tags = soup('span')
for tag in tags:
    sum=int(tag.contents[0])
    suma=suma+sum

print(suma)
    # Look at the parts of a tag
    #print ('TAG:',tag)
    #print ('URL:',tag.get('href', None))
    #print ('Contents:',tag.contents[0])
    #print ('Attrs:',tag.attrs)
