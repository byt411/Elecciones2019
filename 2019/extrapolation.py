import requests
import statistics
from classes import Survey, Results, Province

pp = float(raw_input('Partido Popular: '))
psoe = float(raw_input('Partido Socialista Obrero Espanol: '))
up = float(raw_input('Unidas Podemos: '))
cs = float(raw_input('Ciudadanos: '))
vox = float(raw_input('Vox: '))

percentages = [pp, psoe, up, cs, vox]
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
print "Partido Popular: " + str(pp) + "%"
print "Partido Socialista Obrero Espanol: " + str(psoe) + "%"
print "Unidas Podemos: " + str(up) + "%"
print "Ciudadanos: " + str(cs) + "%"
print "Vox: " + str(vox) + "%"
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
