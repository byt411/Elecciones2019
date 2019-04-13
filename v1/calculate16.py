import requests
import statistics
from classes16 import Survey, SurveyArray2
website_url = requests.get('https://en.wikipedia.org/wiki/Opinion_polling_for_the_2016_Spanish_general_election').text

from bs4 import BeautifulSoup
rawData = BeautifulSoup(website_url, 'lxml')
surveyTable = str(rawData.find('table',{'class':'wikitable collapsible'}))

from lxml import etree
parser = etree.HTMLParser()
tree = etree.fromstring(surveyTable, parser)
surveyRaw = tree.xpath('//tr')
surveys = []
for row in surveyRaw[5:26]:
    newSurvey = Survey(row)
    surveys.append(newSurvey)

data = SurveyArray2(surveys)
print "Partido Popular: " + data.pp
print "Partido Socialista Obrero Espanol: " + data.psoe
print "Unidas Podemos: " + data.up
print "Ciudadanos: " + data.cs
