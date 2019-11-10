import requests
import statistics

from classes import Survey, Results, Province



surveyfile = open("surveys", "r")
surveyRaw = surveyfile.readlines()
surveys = []
for row in surveyRaw:
    surveydata = row.rstrip().split()
    newSurvey = Survey(surveydata)
    surveys.append(newSurvey)

results = Results(surveys)
percentages = [results.pp, results.psoe, results.up, results.cs, results.vox]
print '-----------------------'
provincefile = open("provincedata", "r")
provincedata = provincefile.readlines()
ppseats = 0
psoeseats = 0
upseats = 0
csseats = 0
voxseats = 0
otherseats = 0
navarraseats = 0
for line in provincedata:
    splitLine = line.rstrip().split()
    newProvince = Province(splitLine, percentages)
    ppseats += newProvince.ppseats
    psoeseats += newProvince.psoeseats
    upseats += newProvince.upseats
    csseats += newProvince.csseats
    voxseats += newProvince.voxseats
    otherseats += newProvince.otherseats
    navarraseats += newProvince.navarraseats
print '-----------------------'
print "Partido Popular: " + results.ppstring
print "Partido Socialista Obrero Espanol: " + results.psoestring
print "Unidas Podemos: " + results.upstring
print "Ciudadanos: " + results.csstring
print "Vox: " + results.voxstring
print '-----------------------'
print "Partido Popular: " + str(ppseats)
print "Partido Socialista Obrero Espanol: " + str(psoeseats)
print "Unidas Podemos: " + str(upseats)
print "Ciudadanos: " + str(csseats)
print "Vox: " + str(voxseats)
print "Otros: " + str(otherseats + navarraseats)
print '-----------------------'
print 'PP + Ciudadanos + Vox: ' + str(ppseats + csseats + voxseats + navarraseats)
print 'PSOE + Unidas Podemos: ' + str(psoeseats + upseats)
print 'PSOE + Unidas Podemos + Otros: ' + str(psoeseats + upseats + otherseats)
print 'PSOE + Ciudadanos: ' + str(psoeseats + csseats)
