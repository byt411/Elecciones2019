line = 'Alava 4 0.65460 0.64289 1.30687 0.42067'.rstrip().split()
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
