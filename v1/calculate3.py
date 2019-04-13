import requests
import statistics
from classes import Survey, SurveyArray3
website_url = requests.get('https://es.wikipedia.org/wiki/Anexo:Sondeos_de_intenci%C3%B3n_de_voto_para_las_elecciones_generales_de_Espa%C3%B1a_de_2019').text

from bs4 import BeautifulSoup
rawData = BeautifulSoup(website_url, 'lxml')
surveyTable = str(rawData.find('table',{'class':'wikitable collapsible'}))

from lxml import etree
parser = etree.HTMLParser()
tree = etree.fromstring(surveyTable, parser)
surveyRaw = tree.xpath('//tr')
surveys = []
for row in surveyRaw[2:22]:
    newSurvey = Survey(row)
    surveys.append(newSurvey)

data = SurveyArray3(surveys)
print "Partido Popular: " + data.pp
print "Partido Socialista Obrero Espanol: " + data.psoe
print "Unidas Podemos: " + data.up
print "Ciudadanos: " + data.cs
print "Vox: " + data.vox
