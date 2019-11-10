province = raw_input("Province: ")
seats = raw_input("Seats: ")
pp = raw_input("Partido Popular: ")
psoe = raw_input("Partido Socialista Obrero Espanol: ")
up = raw_input("Unidas Podemos: ")
cs = raw_input("Ciudadanos: ")
vox = raw_input("Vox: ")

pp = float(pp) / 16.70
pp = str(round(pp, 5))
psoe = float(psoe) / 28.68
psoe = str(round(psoe, 5))
up = float(up) / 14.31
up = str(round(up, 5))
cs = float(cs) / 15.86
cs = str(round(cs, 5))
vox = float(vox) / 10.26
vox = str(round(vox, 5))
provincedata = open("2019", "r")
newline = province + " " + seats + " " + pp + " " + psoe + " " + up + " " + cs + " " + vox + "\n"
temp = provincedata.readlines()

temp.insert(0, newline)
provincedata.close()

provincedata = open("2019", "w")
provincedata.writelines(temp)
provincedata.close()
