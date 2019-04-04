import statistics
class Survey:
    def __init__(self, row):
        self.surveyor = row[0].text
        self.date = row[1].text
        self.pp = row[4].text.rstrip()
        self.psoe = row[5][0].text.rstrip()
        self.up = row[6].text.rstrip()
        self.cs = row[7].text.rstrip()
        self.vox = row[14].text.rstrip()

class SurveyArray:
    def __init__(self, array):
        self.array = array
        self.pp = []
        self.psoe = []
        self.up = []
        self.cs = []
        self.vox = []
        for survey in self.array:
            self.pp.append(float(survey.pp))
            self.psoe.append(float(survey.psoe))
            self.up.append(float(survey.up))
            self.cs.append(float(survey.cs))
            self.vox.append(float(survey.vox))
        self.ppmean = str(round(statistics.mean(self.pp), 2)) + "%"
        self.psoemean = str(round(statistics.mean(self.psoe), 2)) + "%"
        self.upmean = str(round(statistics.mean(self.up), 2)) + "%"
        self.csmean = str(round(statistics.mean(self.cs), 2)) + "%"
        self.voxmean = str(round(statistics.mean(self.vox), 2)) + "%"

class SurveyArray2:
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
        old = sum(self.pp[5:21]) / float(15)
        estimate = round((recent * 0.7) + (old * 0.3), 2)
        adjustedestimate = round((20.75 / 19.7) * estimate, 2)
        self.pp = str(adjustedestimate) + "%"

        recent = sum(self.psoe[0:5]) / float(5)
        old = sum(self.psoe[5:21]) / float(15)
        estimate = (recent * 0.7) + (old * 0.3)
        adjustedestimate = round((27.95 / 30.6) * estimate, 2)
        self.psoe = str(adjustedestimate) + "%"

        recent = sum(self.up[0:5]) / float(5)
        old = sum(self.up[5:21]) / float(15)
        estimate = round((recent * 0.7) + (old * 0.3), 2)
        adjustedestimate = round((16.18 / 18.4) * estimate, 2)
        self.up = str(adjustedestimate) + "%"

        recent = sum(self.cs[0:5]) / float(5)
        old = sum(self.cs[5:21]) / float(15)
        estimate = round((recent * 0.7) + (old * 0.3), 2)
        adjustedestimate = round((18.27 / 17.6) * estimate, 2)
        self.cs = str(adjustedestimate) + "%"

        recent = sum(self.vox[0:5]) / float(5)
        old = sum(self.vox[5:21]) / float(15)
        estimate = round((recent * 0.7) + (old * 0.3), 2)
        adjustedestimate = round((10.97 / 10.2) * estimate, 2)
        self.vox = str(adjustedestimate) + "%"
