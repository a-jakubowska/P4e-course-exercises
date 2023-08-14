import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

html=urllib.request.urlopen(url, context=ctx).read()
#print(type(html))

counts=(html.decode().strip())
#print(counts)
stuff=list()

tree= ET.fromstring(counts)

lst= tree.findall('comments/comment/count')
#print('ile:',len(lst))
for i in lst:
    lista=int(i.text)
    #print(type(lista))

    stuff.append(lista)
print(stuff)
x=0
for thing in stuff:
    x=x+thing
print(x)
