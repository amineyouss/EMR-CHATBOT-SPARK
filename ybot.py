import random
from pyspark import SparkContext, SparkConf

#"ouverture de session"

chatbotid=0
clientid=1

#1ere partie Ouverture de la discussion

def func(lines):
		amine=lines.split(" ")
		return (amine[0], 1)
	
def  ouverture(lines):
		amine=lines.split(",")
		return(amine[0], amine[1:])

def  ouverture2(lines):
		amine=lines.split(",")
		return(amine[0], amine[1:])


def amine(word):
             split=word.split(" ")
             return split[0:]

def  ouverture1(lines):
             amine=lines.split(" ")
             return (amine[0], amine[1:])

#def   formulephrase(cat, neg, sent, hs):


		
		

sc =SparkContext()	
rddgree=sc.textFile("greetings.txt")
rddpron=sc.textFile("pronomschatbot.txt")
rddpron=sc.textFile("pronomsclient.txt")
rddsentiments=sc.textFile("sentiments.txt")
rddynov=sc.textFile("ynov.txt")
#rdd4=sc.textFile("adverbes.txt")
#rdd5=sc.textFile("prepositions.txt")
rddsyn=sc.textFile("synonymes.csv")
#rdd2=rdd.flatMapmap("")

##########################################################partie greetings#################################################################################

rddgree1=rddgree.map(ouverture)
rddgree2=rddgree1.lookup('bienvenue')
size=len(rddgree2[0])-1
messagegreetings=rddgree2[0][random.randint(0,size)]
print messagegreetings

#########################################################identification chatbot ###########################################################################
chatbot="je"




###########################################################demande question################################################################################

while True:
	rddsyn1=rddsyn.map(ouverture1)
	messageclient=input()
	#messageclient="es tu un robot?"
	#analysemessage=sc.parallelize(List(messageclient)).collect()
	#print sc.parallelize(List(messageclient)).collect()
	#print messageclientTEXT
	proc=amine(messageclient)
	for i in proc:
			rddsyn2=rddsyn1.lookup(i)
			#rddsyn2.collect()
		 	#print rddsyn2
			rddsentiments1=rddsentiments.map(func)
			rddynov1=rddynov.map(ouverture2)
			rddynov2=rddynov1.lookup(i)
			rddsentiments2=rddsentiments1.lookup(i)
			if (rddsentiments2!=[] ):
				print "merci mon amour"
				print "Je ne suis pas sentimental"
			if (rddynov2!=[]):
				interm=' '.join(str(x) for x in rddynov2[0])
				print interm





#########################################################Fomulations de phrases#############################################################################






