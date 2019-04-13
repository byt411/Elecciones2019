import requests
website_url = requests.get('https://es.wikipedia.org/wiki/Anexo:Sondeos_de_intenci%C3%B3n_de_voto_para_las_elecciones_generales_de_Espa%C3%B1a_de_2019').text

from bs4 import BeautifulSoup
rawData = BeautifulSoup(website_url, 'lxml')
surveyTable = str(rawData.find('table',{'class':'wikitable collapsible'}))

from lxml import etree
parser = etree.HTMLParser()
tree = etree.fromstring(surveyTable, parser)
ppraw = tree.xpath('//tr/td[position()=5]')
psoeraw = tree.xpath('//tr/td[position()=6]')
podemosraw = tree.xpath('//tr/td[position()=7]')
ciudadanosraw = tree.xpath('//tr/td[position()=8]')
voxraw = tree.xpath('//tr/td[position()=15]')

pp = []
for r in ppraw:
    if str(r.text) != 'None' and str(r.text) != '':
      pp.append(float(r.text))


from statistics import mean
ppmean = str(round(mean(pp), 2)) + '%'
print 'Partido Popular: ' + ppmean
