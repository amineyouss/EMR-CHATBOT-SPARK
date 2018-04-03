import unidecode
import wget
filer=open("/root/Desktop/learn/2.txt", "r")

lines=filer.read()
verbes=lines.split("  ")
print verbes
print len(verbes)
for i in verbes:
	url="https://leconjugueur.lefigaro.fr/exporter/verbe/"+i+".rtf"	
	filename = wget.download(url)
