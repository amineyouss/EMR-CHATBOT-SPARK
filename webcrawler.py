from lxml import html
import requests
import urllib3
#page=requests.get("https://leconjugueur.lefigaro.fr/conjugaison/verbe/aimer.html")
#tree=html.fromstring(page.content)
#print tree

links=[]
http = urllib3.PoolManager()
r = http.request('GET', 'https://leconjugueur.lefigaro.fr/conjugaison/verbe/aimer.html')
print r.data
full=r.data

liste=full.xpath('//div[@class="tempbloc"]/text()')

print liste
