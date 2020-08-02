from bs4 import BeautifulSoup
import requests
url= input("Enter your URL:")
req = requests.get(url, allow_redirects=True)
print("Content Type:")
print (req.headers.get('content-type'))
print("Etag:")
print (req.headers.get('ETag'))
print("Content Length:")
print (req.headers.get('content-length'))
print("Server:")
print (req.headers.get('Server'))
print("Date:")
print (req.headers.get('Date'))
print("Connection:")
print (req.headers.get('Connection'))
print("Keep Alive:")
print (req.headers.get('Keep-Alive'))
print("Upgrade:")
print (req.headers.get('Upgrade'))
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
print(soup.title.text)  
print("ALL THE LINKS PRESENT IN THE PAGE :")
for link in soup.find_all('a'):
 print(link.get('href'))


