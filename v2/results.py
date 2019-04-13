import requests
import statistics
from bs4 import BeautifulSoup
from lxml import etree
from classes import Survey, Results

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
print "Partido Popular: " + results.ppstring
print "Partido Socialista Obrero Espanol: " + results.psoestring
print "Unidas Podemos: " + results.upstring
print "Ciudadanos: " + results.csstring
print "Vox: " + results.voxstring

#provincefile = open("provincedata", "r")
#provincedata = provincefile.readlines()
#provinceArray = []
#for line in provincedata:
#    splitLine = provincedata.rstrip().split()
#    newProvince = Province(splitLine)
#    provinceArray.append(newProvince)
