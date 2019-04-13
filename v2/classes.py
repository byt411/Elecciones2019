class Survey:
    def __init__(self, row):
        self.surveyor = row[0].text
        self.date = row[1].text
        self.pp = row[4].text.rstrip()
        self.psoe = row[5][0].text.rstrip()
        self.up = row[6].text.rstrip()
        self.cs = row[7].text.rstrip()
        self.vox = row[14].text.rstrip()

pp15Multi = 28.72 / 28.1
pp18Multi = 20.7 / 19.7
psoe15Multi = 22.01 / 23.9
psoe18Multi = 27.9 / 30.6
up15Multi = 20.66 / 15.3
up18Multi = 16.2 / 18.4
cs15Multi = 13.93 / 18.6
cs18Multi = 18.3 / 17.6
voxMulti = 11.0 / 10.2

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
        recent = sum(self.pp[0:5]) / float(5)
        medium = sum(self.pp[5:11]) / float(5)
        old = sum(self.pp[11:21]) / float(10)
        estimate = (recent * 0.45) + (medium * 0.25) + (old * 0.1)
        adjustedestimate = estimate * ((0.6 * pp15Multi) + (0.4 * pp18Multi))
        self.pp = adjustedestimate
        self.ppstring = str(round(self.pp, 2)) + "%"

        recent = sum(self.psoe[0:5]) / float(5)
        medium = sum(self.psoe[5:11]) / float(5)
        old = sum(self.psoe[11:21]) / float(10)
        estimate = (recent * 0.45) + (medium * 0.35) + (old * 0.20)
        adjustedestimate = estimate * ((0.6 * psoe15Multi) + (0.4 * psoe18Multi))
        self.psoe = adjustedestimate
        self.psoestring = str(round(self.psoe, 2)) + "%"

        recent = sum(self.up[0:5]) / float(5)
        medium = sum(self.up[5:11]) / float(5)
        old = sum(self.up[11:21]) / float(10)
        estimate = (recent * 0.45) + (medium * 0.35) + (old * 0.20)
        adjustedestimate = estimate * ((0.6 * up15Multi) + (0.4 * up18Multi))
        self.up = adjustedestimate
        self.upstring = str(round(self.up, 2)) + "%"

        recent = sum(self.cs[0:5]) / float(5)
        medium = sum(self.cs[5:11]) / float(5)
        old = sum(self.cs[11:21]) / float(10)
        estimate = (recent * 0.45) + (medium * 0.35) + (old * 0.20)
        adjustedestimate = estimate * ((0.6 * cs15Multi) + (0.4 * cs18Multi))
        self.cs = adjustedestimate
        self.csstring = str(round(self.cs, 2)) + "%"

        recent = sum(self.vox[0:5]) / float(5)
        medium = sum(self.vox[5:11]) / float(5)
        old = sum(self.vox[11:21]) / float(10)
        estimate = (recent * 0.45) + (medium * 0.35) + (old * 0.20)
        adjustedestimate = estimate * voxMulti
        self.vox = adjustedestimate
        self.voxstring = str(round(self.vox, 2)) + "%"

class Province:
        def __init__(self, line):
            self.name = line[0]
            self.seats = int(line[1])
            self.ppmulti = float(line[2])
            self.psoemulti = float(line[3])
            self.upmulti = float(line[4])
            self.csmulti = float(line[5])
            self.voxmulti = float(line[6])

            self.ppseats = 0
            self.psoeseats = 0
            self.upseats = 0
            self.csseats = 0
            self.voxseats = 0
