import requests
import statistics
from classes import Survey, SurveyArray
website_url = requests.get('https://es.wikipedia.org/wiki/Anexo:Sondeos_de_intenci%C3%B3n_de_voto_para_las_elecciones_generales_de_Espa%C3%B1a_de_2019').text

from bs4 import BeautifulSoup
rawData = BeautifulSoup(website_url, 'lxml')
surveyTable = str(rawData.find('table',{'class':'wikitable collapsible'}))

from lxml import etree
parser = etree.HTMLParser()
tree = etree.fromstring(surveyTable, parser)
surveyRaw = tree.xpath('//tr')

resultNum = raw_input('Introduzca el numero de encuestas: ')
surveys = []
for row in surveyRaw[2:(int(resultNum) + 2)]:
    newSurvey = Survey(row)
    surveys.append(newSurvey)

data = SurveyArray(surveys)
print "Partido Popular: " + data.ppmean
print "Partido Socialista Obrero Espanol: " + data.psoemean
print "Unidas Podemos: " + data.upmean
print "Ciudadanos: " + data.csmean
print "Vox: " + data.voxmean
