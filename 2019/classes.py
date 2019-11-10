import operator
class Survey:
    def __init__(self, row):
        self.pp = row[0].rstrip()
        self.psoe = row[1].rstrip()
        self.up = row[2].rstrip()
        self.cs = row[3].rstrip()
        self.vox = row[4].rstrip()


ppMulti = 16.7 / 17.2
psoeMulti = 28.68 / 30.2
upMulti = 14.31 / 12.9
csMulti = 15.86 / 13.6
voxMulti = 10.26 / 11.9

class Results:
    def __init__(self, array):
        self.array = array
        self.pp = []
        self.psoe = []
        self.up = []
        self.cs = []
        self.vox = []
        self.parties = [self.pp, self.psoe, self.up, self.cs, self.vox]
        for survey in self.array:
            self.pp.append(float(survey.pp))
            self.psoe.append(float(survey.psoe))
            self.up.append(float(survey.up))
            self.cs.append(float(survey.cs))
            self.vox.append(float(survey.vox))

        veryrecent = sum(self.pp[0:6]) / float(5)
        recent = sum(self.pp[6:11]) / float(5)
        medium = sum(self.pp[11:26]) / float(15)
        old = sum(self.pp[26:]) / float(len(array) - 25)
        estimate = (veryrecent * 0.40) + (recent * 0.30) + (medium * 0.20) + (old * 0.10)
        self.pp = estimate * ppMulti
        self.ppstring = str(round(self.pp, 2)) + "%"

        veryrecent = sum(self.psoe[0:6]) / float(5)
        recent = sum(self.psoe[6:11]) / float(5)
        medium = sum(self.psoe[11:26]) / float(15)
        old = sum(self.psoe[26:]) / float(len(array) - 25)
        estimate = (veryrecent * 0.40) + (recent * 0.30) + (medium * 0.20) + (old * 0.10)
        self.psoe = estimate * psoeMulti
        self.psoestring = str(round(self.psoe, 2)) + "%"

        veryrecent = sum(self.up[0:6]) / float(5)
        recent = sum(self.up[6:11]) / float(5)
        medium = sum(self.up[11:26]) / float(15)
        old = sum(self.up[26:]) / float(len(array) - 25)
        estimate = (veryrecent * 0.40) + (recent * 0.30) + (medium * 0.20) + (old * 0.10)
        self.up = estimate * upMulti
        self.upstring = str(round(self.up, 2)) + "%"

        veryrecent = sum(self.cs[0:6]) / float(5)
        recent = sum(self.cs[6:11]) / float(5)
        medium = sum(self.cs[11:26]) / float(15)
        old = sum(self.cs[26:]) / float(len(array) - 25)
        estimate = (veryrecent * 0.40) + (recent * 0.30) + (medium * 0.20) + (old * 0.10)
        self.cs = estimate * csMulti
        self.csstring = str(round(self.cs, 2)) + "%"

        veryrecent = sum(self.vox[0:6]) / float(5)
        recent = sum(self.vox[6:11]) / float(5)
        medium = sum(self.vox[11:26]) / float(15)
        old = sum(self.vox[26:]) / float(len(array) - 25)
        estimate = (veryrecent * 0.40) + (recent * 0.30) + (medium * 0.20) + (old * 0.10)
        self.vox = estimate * voxMulti
        self.voxstring = str(round(self.vox, 2)) + "%"

class Province:
        def __init__(self, line, percentages):
            self.name = line[0]
            self.seats = int(line[1])
            self.ppmulti = float(line[2])
            self.psoemulti = float(line[3])
            self.upmulti = float(line[4])
            self.csmulti = float(line[5])
            self.voxmulti = float(line[6])
            self.pp = self.ppmulti * percentages[0]
            self.psoe = self.psoemulti * percentages[1]
            self.up = self.upmulti * percentages[2]
            self.cs = self.csmulti * percentages[3]
            self.vox = self.voxmulti * percentages[4]
            other = 95 - self.pp - self.psoe - self.up - self.cs - self.vox
            self.other1 = other
            if self.name == "Navarra":
                self.navarra = self.pp + self.cs
                self.other1 = other / 2
                self.other2 = other / 2


            self.ppseats = 0
            self.psoeseats = 0
            self.upseats = 0
            self.csseats = 0
            self.voxseats = 0
            self.otherseats = 0
            self.navarraseats = 0

            self.seatcount = 1
            self.seatlist = []
            while self.seatcount - 1 < self.seats:
                if self.name != "Navarra":
                    seatentry = ('PP', (self.pp / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('PSOE', (self.psoe / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('UP', (self.up / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Cs', (self.cs / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Vox', (self.vox / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Other1', (self.other1 / self.seatcount))
                    self.seatlist.append(seatentry)
                else:
                    seatentry = ('PSOE', (self.psoe / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('UP', (self.up / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Navarra', (self.navarra / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Vox', (self.vox / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Other1', (self.other1 / self.seatcount))
                    self.seatlist.append(seatentry)
                    seatentry = ('Other2', (self.other2 / self.seatcount))
                    self.seatlist.append(seatentry)
                self.seatcount += 1
            self.seatlist.sort( key = operator.itemgetter(1), reverse = True)
            self.seatlist = self.seatlist[0:self.seats]

            for seat in self.seatlist:
                if seat[0] == 'PP':
                    self.ppseats += 1
                elif seat[0] == 'PSOE':
                    self.psoeseats += 1
                elif seat[0] == 'UP':
                    self.upseats += 1
                elif seat[0] == 'Cs':
                    self.csseats += 1
                elif seat[0] == 'Vox':
                    self.voxseats += 1
                elif seat[0] == 'Other1' or seat[0] == 'Other2':
                    self.otherseats += 1
                elif seat[0] == "Navarra":
                    self.navarraseats += 1
            print self.name + ' ' + str(self.ppseats) + ' ' + str(self.psoeseats) + ' ' + str(self.upseats) + ' ' + str(self.csseats) + ' ' + str(self.voxseats) + ' ' + str(self.otherseats)
