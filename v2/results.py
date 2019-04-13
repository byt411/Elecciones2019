import requests
import statistics
from bs4 import BeautifulSoup
from lxml import etree
from classes import Survey, Results, Province

website_url = requests.get('https://es.wikipedia.org/wiki/Anexo:Sondeos_de_intenci%C3%B3n_de_voto_para_las_elecciones_generales_de_Espa%C3%B1a_de_2019').text
rawData = BeautifulSoup(website_url, 'lxml')
surveyTable = str(rawData.find('table',{'class':'wikitable collapsible'}))

parser = etree.HTMLParser()
tree = etree.fromstring(surveyTable, parser)
surveyRaw = tree.xpath('//tr')
surveys = []
for row in surveyRaw[2:22]:
    newSurvey = Survey(row)
    surveys.append(newSurvey)

results = Results(surveys)
percentages = [results.pp, results.psoe, results.up, results.cs, results.vox]
print "Partido Popular: " + results.ppstring
print "Partido Socialista Obrero Espanol: " + results.psoestring
print "Unidas Podemos: " + results.upstring
print "Ciudadanos: " + results.csstring
print "Vox: " + results.voxstring
print '-----------------------'
provincefile = open("provincedata", "r")
provincedata = provincefile.readlines()
ppseats = 0
psoeseats = 0
upseats = 0
csseats = 0
voxseats = 0
otherseats = 0
for line in provincedata:
    splitLine = line.rstrip().split()
    newProvince = Province(splitLine, percentages)
    ppseats += newProvince.ppseats
    psoeseats += newProvince.psoeseats
    upseats += newProvince.upseats
    csseats += newProvince.csseats
    voxseats += newProvince.voxseats
    otherseats += newProvince.otherseats

print "Partido Popular: " + str(ppseats)
print "Partido Socialista Obrero Espanol: " + str(psoeseats)
print "Unidas Podemos: " + str(upseats)
print "Ciudadanos: " + str(csseats)
print "Vox: " + str(voxseats)
print "Otros: " + str(otherseats)
print '-----------------------'
print 'PP + Ciudadanos + Vox: ' + str(ppseats + csseats + voxseats)
print 'PSOE + Unidas Podemos: ' + str(psoeseats + upseats)
print 'PSOE + Unidas Podemos + Otros: ' + str(psoeseats + upseats + otherseats)
print 'PSOE + Ciudadanos: ' + str(psoeseats + csseats)
