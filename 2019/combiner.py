file15 = open("2015", "r")
data15 = file15.readlines()
file15.close()

file16 = open("2016", "r")
data16 = file16.readlines()
file16.close()
output = open("provincedata", "w")

count = 0
while count < 52:
    line15 = data15[count].rstrip().split()
    line16 = data16[count].rstrip().split()
    name = line15[0]
    seats = line15[1]
    ppMulti = str(round((float(line15[2]) * 0.4) + (float(line16[2]) * 0.6), 5))
    psoeMulti = str(round((float(line15[3]) * 0.4) + (float(line16[3]) * 0.6), 5))
    upMulti = str(round((float(line15[4]) * 0.4) + (float(line16[4]) * 0.6), 5))
    csMulti = str(round((float(line15[5]) * 0.4) + (float(line16[5]) * 0.6), 5))

    newline = name + " " + seats + " " + ppMulti + " " + psoeMulti + " " + upMulti + " " + csMulti + "\n"
    output.write(newline)
    print "Complete for " + name
    count += 1

output.close()
