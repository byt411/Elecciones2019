line = 'Vizcaya 8 0.39624 0.58928 1.26331 0.27495'.rstrip().split()
percentages = [28.72, 22.01, 20.66, 13.93, 0.23]
import classes as x
new = x.Province(line, percentages)
print 'PP: ' + str(new.ppseats)
print 'PSOE: ' + str(new.psoeseats)
print 'Unidas Podemos: ' + str(new.upseats)
print 'Ciudadanos: ' + str(new.csseats)
print 'Vox: ' + str(new.voxseats)
print 'Otros: ' + str(new.otherseats)
print new.seatlist
