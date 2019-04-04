import statistics
class Survey:
    def __init__(self, row):
        self.surveyor = row[0].text
        self.date = row[1].text
        self.pp = row[4][0].text.rstrip()
        self.psoe = row[5].text.rstrip()
        self.up = row[15].text.rstrip()
        self.cs = row[7].text.rstrip()
class SurveyArray2:
    def __init__(self, array):
        self.array = array
        self.pp = []
        self.psoe = []
        self.up = []
        self.cs = []
        for survey in self.array:
            self.pp.append(float(survey.pp))
            self.psoe.append(float(survey.psoe))
            self.up.append(float(survey.up))
            self.cs.append(float(survey.cs))
        recent = sum(self.pp[0:3]) / float(3)
        medium = sum(self.pp[3:11]) / float(8)
        old = sum(self.pp[11:21]) / float(10)
        estimate = round((recent * 0.6) + (medium * 0.3) + (old * 0.1), 2)
        adjustedestimate = (20.75 / 19.7) * estimate
        correctedestimate = round(adjustedestimate * (33 / 31.19), 2)
        self.pp = str(correctedestimate) + "%"

        recent = sum(self.psoe[0:3]) / float(3)
        medium = sum(self.psoe[3:11]) / float(8)
        old = sum(self.psoe[11:21]) / float(10)
        estimate = round((recent * 0.6) + (medium * 0.3) + (old * 0.1), 2)
        adjustedestimate = round((27.95 / 30.6) * estimate, 2)
        correctedestimate = round(adjustedestimate * (22.6 / 19.87), 2)
        self.psoe = str(correctedestimate) + "%"

        recent = sum(self.up[0:3]) / float(3)
        medium = sum(self.up[3:11]) / float(8)
        old = sum(self.up[11:21]) / float(10)
        estimate = round((recent * 0.6) + (medium * 0.3) + (old * 0.1), 2)
        adjustedestimate = round((16.18 / 18.4) * estimate, 2)
        correctedestimate = round(adjustedestimate * (21.2 / 21.39), 2)
        self.up = str(correctedestimate) + "%"

        recent = sum(self.cs[0:3]) / float(3)
        medium = sum(self.cs[3:11]) / float(8)
        old = sum(self.cs[11:21]) / float(10)
        estimate = round((recent * 0.6) + (medium * 0.3) + (old * 0.1), 2)
        adjustedestimate = round((18.27 / 17.6) * estimate, 2)
        correctedestimate = round(adjustedestimate * (13.1 / 14.15), 2)
        self.cs = str(correctedestimate) + "%"
