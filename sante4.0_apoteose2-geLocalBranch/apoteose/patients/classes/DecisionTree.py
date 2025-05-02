
class DecisionTree(object):
    def __init__(self):
        self.DictionaryThresholdFRAX = {
                "50" : 5,
                "51" : 5.3,
                "52" : 5.5,
                "53" : 5.7,
                "54" : 5.9,
                "55" : 6,
                "56" : 6.1,
                "57" : 6.3,
                "58" : 6.4,
                "59" : 6.6,
                "60" : 6.9,
                "61" : 7.5,
                "62" : 8,
                "63" : 8.5,
                "64" : 8.9,
                "65" : 9.3,
                "66" : 10,
                "67" : 11,
                "68" : 12,
                "69" : 13,
                "70" : 13,
                "71" : 15,
                "72" : 16,
                "73" : 17,
                "74" : 18,
                "75" : 19,
                "76" : 21,
                "77" : 22,
                "78" : 24,
                "79" : 25,
                "80" : 27,
                "81" : 29,
                "82" : 30,
                "83" : 32,
                "84" : 34,
                "85" : 35,
                "86" : 36,
                "87" : 36,
                "88" : 36,
                "89" : 36,
                "90" : 13}
        
        self.Path = []

    def DecisionChoice(self, Patient):
        self.Path.append(self.lowestZScore(Patient))

        if Patient["age"] <= 24:
            self.Path.append("->")
            self.Path.append("Pediatrique")
            self.PossiblePediatrique(Patient)
            self.HeightLoss(Patient)

            return self.Path
        
        if Patient["corticotherapie"] == "Oui":
            # Third Situation
            self.Path.append("->")
            self.Path.append("Corticotherapie")
            self.PossibleTreatmentsThirdSituation(Patient)

        if Patient["cancer_sein"] == "Oui":
            # Fourth Situation
            self.Path.append("->")
            self.Path.append("CancerDuSein")
            self.PossibleTreatmentsFourthSituation(Patient)

        if Patient["cancer_prostate"] == "Oui":
            # Fifth Situation
            self.Path.append("->")
            self.Path.append("CancerDuProstate")
            self.PossibleTreatmentsFifthSituation(Patient)
        
        if Patient["sexe"] == "Masculin":
            self.Path.append("->")
            self.Path.append("M")
            self.PossibleTreatmentsSixthSituation(Patient)

        if Patient["sexe"] == "Feminin":
            self.Path.append("->")
            self.Path.append("W")
            
            if Patient["menopause"] == "Oui":
                # First Situation
                self.Path.append("menopause")
                self.PossibleTreatmentsFirstSituation(Patient)
            else:
                # Woman with no Menopause
                self.Path.append("NoMenopause")
                self.Path.insert(0, False)
        
         # now the idea is to use this method to insert in the first place True or False 
        self.Path.insert(0, "<<<<-")
        self.Output = False
        for i in range(len(self.Path)): # if in one the situations analyzed the diagnose has been true, the software returns TRUE
            if self.Path[i] == True:
                self.Output = True
        self.Path.insert(0, self.Output)

        return self.Path
    

    def PossiblePediatrique(self, Patient):
        if (self.lowestZScore(Patient)) > -2:
            self.Path.append("Tscore>-2")
            self.Path.insert(0, False)
        else:
            self.Path.append("Tscore<=-2")
            self.Path.insert(0, True)
    

    def HeightLoss(self, Patient):
        if Patient["age"] <= 20 or Patient["taille_20"] == None:
            pass
        else:
            height_diff = Patient["taille"] - Patient["taille_20"]
            if height_diff < 4:
                self.Path.append("Perte de taille de 2 cm : Pas besoin de radiographie")


    def PossibleTreatmentsFirstSituation(self, Patient):
        # Menopause
        if Patient["fracture_severe"] == "Oui":
            self.Path.append("FS")
            return self.MenopauseWithFracturesSevere(Patient)
        elif Patient["fracture_non_severe"] == "Oui":
            self.Path.append("FNS")
            return self.MenopauseWithFracturesNoSevere(Patient)
        else:
            if (self.lowestZScore(Patient)) <= -3.0:
                self.Path.append("Tscore<=-3")
                self.Path.insert(0, True)
            elif (self.lowestZScore(Patient)) > -3.0 and (self.lowestZScore(Patient)) <= -2.0:
                self.Path.append("-2>=Tscore>-3")
                self.ChoiceByFRAX(Patient)
            else:
                self.Path.append("Tscore>-2")
                self.Path.insert(0, False)
    

    def MenopauseWithFracturesSevere(self, Patient):
        if (self.lowestZScore(Patient)) >= -1.0:
            self.Path.append("Tscore>=-1")
            return self.ChoiceByFRAX(Patient)
        else:
            self.Path.append("Tscore<-1")
            self.Path.insert(0, True)


    def PossibleTreatmentsThirdSituation(self, Patient): # corticotherapie
        a = False # this is for recording the situation

        if Patient["sexe"] == "Masculin":
            self.Path.append("M")
            if (Patient["age"] >= 50):
                self.Path.append("Plus50")
                a = True
            else:
                self.Path.append("Moins50")
        
        else: # woman
            self.Path.append("F")
            if Patient["menopause"] == "Oui":
                self.Path.append("Menopause")
                a = True
            else:
                self.Path.append("NoMenopause")
        
        if a == True: # Create the Decision Tree
            if Patient["fracture_non_severe"] == "Oui":
                self.Path.append("FNS50")
                self.Path.insert(0, True)
                return
            else:
                if Patient["age"] >= 70:
                    self.Path.append("Plus70")
                    self.Path.insert(0, True)
                else:
                    if self.lowestZScore(Patient) <= -2.5:
                        self.Path.append("TScore<=-2.5")
                        self.Path.insert(0, True)
                        return
                    else:
                        if Patient["corticotherapie_plus_7_5"] == "Oui":
                            self.Path.append("Corticotherapie>=7.5")
                            self.Path.insert(0, True)
                        else:
                            self.ChoiceByFRAX(Patient)
                            return
        else: 
            if Patient["antecedent_fracture_faible_energie"] == "Oui":
                self.Path.append("FFE")
                self.Path.insert(0, True)
            else:
                self.ChoiceByFRAX(Patient)


    def PossibleTreatmentsFourthSituation(self, Patient):
        if Patient["menopause"] == "Oui":
            self.Path.append("F")
            self.Path.append("Menopause")
            if Patient["fracture_severe"] == "Oui":
                self.Path.append("FS")
                self.Path.insert(0, True)
            else:
                if self.lowestZScore(Patient) >= -1:
                    self.Path.append("TScore>=-1")
                    self.Path.insert(0, False)
                elif self.lowestZScore(Patient) <= -2.5:
                    self.Path.append("TScore<=-2.5")
                    self.Path.insert(0, True)
                else:
                    self.ChoiceByFRAX(Patient)
        else:
            self.Path.append("F")
            self.Path.append("NoMenopause")
            if (Patient["analogue_lh_rh"] == "Oui" and Patient["tamoxifene"] == "Oui") \
                or (Patient["analogue_lh_rh"] == "Oui" and Patient["horm_anastrazole"] == "Oui") \
                or (Patient["analogue_lh_rh"] == "Oui" and Patient["horm_letrozole"] == "Oui") \
                or (Patient["analogue_lh_rh"] == "Oui" and Patient["horm_exemestane"] == "Oui") \
                or (Patient["amenorrhee_induite"] == "Oui"):

                # Write the motivation
                if Patient["amenorrhee_induite"] == "Oui":
                    self.Path.append("Amenorrhee induite")
                else:
                    self.Path.append("Analogue de LH-RH")

                if Patient["fracture_severe"] == "Oui":
                    self.Path.append("FS")
                    self.Path.insert(0, True)
                else:
                    if self.lowestZScore(Patient) >= -1:
                        self.Path.append("TScore>=-1")
                        self.Path.insert(0, False)
                    elif self.lowestZScore(Patient) <= -2.5:
                        self.Path.append("TScore<=-2.5")
                        self.Path.insert(0, True)
                    else:
                        self.ChoiceByFRAX(Patient)
            elif Patient["amenorrhee_induite"] == "Non":
                self.Path.append("Non aménorrhée induite")
                self.Path.insert(0, False)


    def PossibleTreatmentsFifthSituation(self, Patient): # cancer du prostate
        if Patient["fracture_severe"] == "Oui":
            self.Path.append("FS")
            self.Path.insert(0, True)
        else:
            if self.lowestZScore(Patient) > -1.5:
                self.Path.append("TScore>-1.5")
                self.Path.insert(0, False)
            elif self.lowestZScore(Patient) <= -2.5:
                self.Path.append("TScore<=-2.5")
                self.Path.insert(0, True)
            else:
                if self.CheckDuexFractures(Patient) >= 2:
                    self.Path.append("-1.5>=TScore>-2.5")
                    self.Path.append("DeuxFractures")
                    self.Path.insert(0, True)
                else:
                    if Patient["frax"] > 20.0:
                        self.Path.append("-1.5>=TScore>-2.5")
                        self.Path.append("FraxMajeurs>20")
                        self.Path.insert(0, True)
                    else:
                        if Patient["frax_cancer"] >= 3.0:
                            self.Path.append("-1.5>=TScore>-2.5")
                            self.Path.append("frax_cancer>3")
                            self.Path.insert(0, True)
                        else:
                            self.Path.append("-1.5>=TScore>-2.5")
                            self.Path.insert(0, False)
    

    def CheckDuexFractures(self, Patient):
        Nombre = 0
        if Patient["age"] >= 75:
            self.Path.append("Plus75")
            Nombre = Nombre + 1
        if Patient["IMClow"] == "Oui":
            Nombre = Nombre + 1
            self.Path.append("IMClow")
        if Patient["corticotherapie_plus_3"] == "Oui":
            self.Path.append("Corticotherapie Actuelle")
            Nombre = Nombre + 1
        if Patient["fracture_non_severe"] == "Oui":
            self.Path.append("FNS50")
            Nombre = Nombre + 1
        if Patient["chutes_frequentes"] == "Oui":
            self.Path.append("Chutes à répetition")
            Nombre = Nombre + 1
        if Patient["comorbites_associees"] == "Oui":
            self.Path.append("3 Comorbidités Associées")
            Nombre = Nombre + 1
        return Nombre
    

    def PossibleTreatmentsSixthSituation(self, Patient):
        # Men
        lZscore = self.lowestZScore(Patient)

        if lZscore > -1:
            self.Path.append("Tscore>-1")
            self.Path.insert(0, True)
        elif lZscore <= -1 and Patient["fracture_severe"] == "Oui":
            self.Path.append("Tscore<=-1")
            self.Path.append("FS")
            self.Path.insert(0, True)
        elif lZscore <= -2 and Patient["fracture_non_severe"] == "Oui":
            self.Path.append("Tscore<=-2")
            self.Path.append("FFE")
            self.Path.insert(0, True)
        elif lZscore <= -3:
            self.Path.append("Tscore<=-3")
            self.Path.insert(0, True)
        else:
            self.Path.insert(0, False)
    

    def lowestZScore(self, Patient):
        self.min = 1000

     #   if Patient["z_score_femur_popup"] == True or float(Patient["z_score_col_femur"]) < self.min:
      #      self.min = Patient["z_score_col_femur"]
       # if Patient["z_score_hanche_popup"] == True or float(Patient["z_score_hache"]) < self.min:
       #     self.min = Patient["z_score_hache"]
        #if Patient["z_score_rachis_popup"] == True or float(Patient["z_score_rachis"]) < self.min:
         #   self.min = Patient["z_score_rachis"]
        # if Patient["z_score_extremite_popup"] == True or Patient["z_score_extremite_distale"] < self.min:
        #     self.min = Patient["z_score_extremite_distale"]

        return self.min
    

    def ChoiceByFRAX(self, Patient):
        if Patient["frax"] >= self.DictionaryThresholdFRAX[Patient["age"]]:
            self.Path.append("FraxAbove")
            self.Path.insert(0, True)
            return
        else:
            self.Path.append("FraxLow")
            self.Path.insert(0, False)
            return
       