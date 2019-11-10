pp = raw_input("Partido Popular: ")
psoe = raw_input("Partido Socialista Obrero Espanol: ")
up = raw_input("Unidas Podemos: ")
cs = raw_input("Ciudadanos: ")
vox = raw_input("Vox: ")

surveys = open("surveys", "r")
newline = pp + " " + psoe + " " + up + " " + cs + " " + vox + "\n"
temp = surveys.readlines()

temp.insert(0, newline)
surveys.close()

surveys = open("surveys", "w")
surveys.writelines(temp)
surveys.close()
