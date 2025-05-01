from apoteose.patients.classes.DecisionTree import DecisionTree


class Traitements:
    def __init__(self, Patient):
        self.Patient = Patient
        self.listOutput = []
        self.Dict_All_Traitements = {
            "ALN" :  "Acide alendronique (aledronate) 70 mg hebdomadaire (ou 10 mg/jour)", # woman 
            "ALN1" :  "Acide alendronique (aledronate) 70 mg hebdomadaire", # cancer du sein # cancer du prostate
            "RIS" :  "Acide risédronique (risédronate) 35 mg hebdomadaire ou 75 mg 1 comprimé 2 j de suite 1 fois par mois (ou 5 mg/j)", # cortisonique # woman
            "RIS1" :  "Acide risédronique (risédronate) 35 mg hebdomadaire, recommandé en premiére intention", # cancer du sein
            "RIS2" :  "Acide risédronique (risédronate) 35 mg hebdomadaire", # cancer du prostate
            "ZOL" :  "Acide zolédronique (zolédronate) 5 mg 1 perfusionune fois par an" , # cancer du sein # cortisonique # woman
            "DEN" :  "Denosumab 60 mg 1 injection SC tous les 6 mois, recommandés en relais des bisphosphonates", # woman
            "DEN1" :  "Denosumab 60 mg 1 injection SC tous les 6 mois, pourrait être une alternative chez les femmes ménopausées mais ne peut être recommandé en l'absence d'AMM dans cette population. Il ne peut être discuté qu'en 2eme intention et un relais par bisphosphonates doit être prévu.", # cancer du sein
            "DEN2" :  "Denosumab 60 mg 1 injection SC tous les 6 mois est indiqué en cas de contre-indications ou d'intolérance aux bisphosphonates", # cancer du la prostate
            "RAL" :  "Raloxifène (60 mg/jour), remboursé jusqu'à 70 ans",
            "RAL1" :  "Raloxifène (60 mg/jour)",
            "TER" :  "Tériparatide 20 ug/j remboursé avec au moins deux fractures vertébrales",
            "TER1" :  "Tériparatide 20 ug/j n'est pas remboursé dans les recommandations même en l'absance de radiothérapie", # cancer du sein
            "THM" :  "Traitement hormonal de la ménopause (THM) entre 50 et 60 ans si troubles du climatère",

            # Now I added these record just to differentiate the situation and printing in a better way
            # I wonted to follow with the same structur
            "WOMEN":  "---- Femme Menopause----",
            "MAN":  "---- Homme ----",
            "SEIN":  "---- Cancer du sein ----" ,
            "PROS":  "---- Cancer du la prostate ----",
            "CORT":  "---- Corticotherapie ----"
        }

        self.DefineListOfTraitement()
    
    def DefineListOfTraitement(self):
        self.DT = DecisionTree().DecisionChoice(self.Patient)
        self.Enter = False #check if we have entered inside a possibility

        # pediatrique -> return without any treatment
        if self.Patient["age"] <= 24:
            return
        
        # corticotherapie
        if self.Patient["corticotherapie"] == "Oui" and self.DT[0] == True:
            self.listOutput.append(self.Dict_All_Traitements.get("CORT"))
            self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
            self.listOutput.append(self.Dict_All_Traitements.get("RIS"))
            if self.Patient["fracture_severe"] == "Oui" and self.Patient["fracture_deux_vertebres"] == "Oui":
                self.listOutput.append(self.Dict_All_Traitements.get("TER"))
            self.Enter = True
        
        # cancer du prostate
        if self.Patient["cancer_prostate"] == "Oui" and self.DT[0] == True:
            self.listOutput.append(self.Dict_All_Traitements.get("PROS"))
            self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
            self.listOutput.append(self.Dict_All_Traitements.get("RIS2"))
            self.listOutput.append(self.Dict_All_Traitements.get("ALN1"))
            self.listOutput.append(self.Dict_All_Traitements.get("DN2"))
            self.Enter = True
        
        # cancer du sein
        if self.Patient["cancer_sein"] == "Oui" and self.DT[0] == True:
            self.listOutput.append(self.Dict_All_Traitements.get("SEIN"))
            self.listOutput.append(self.Dict_All_Traitements.get("RIS1"))
            self.listOutput.append(self.Dict_All_Traitements.get("ALN1"))
            self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
            self.listOutput.append(self.Dict_All_Traitements.get("DEN1"))
            self.listOutput.append(self.Dict_All_Traitements.get("TER1"))
            self.Enter = True
        
        # men
        if self.DT[0] == True and self.Enter == False and self.Patient["sexe"] == "Masculin": #man without any other problem
            self.listOutput.append(self.Dict_All_Traitements.get("MAN"))
            self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
            self.listOutput.append(self.Dict_All_Traitements.get("RIS"))
            if self.Patient["fracture_severe"] == "Oui":
                self.listOutput.append(self.Dict_All_Traitements.get("TER"))

        # general definition menopause
        if self.DT[0] == True and self.Enter == False and self.Patient["sexe"] == "Féminin":
            self.listOutput.append(self.Dict_All_Traitements.get("WOMEN"))
            if self.Patient["fracture_severe"] == "Oui":
                self.listOutput.append(self.Dict_All_Traitements.get("ALN"))
                self.listOutput.append(self.Dict_All_Traitements.get("RIS"))
                self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
                self.listOutput.append(self.Dict_All_Traitements.get("DEN"))

                if self.Patient["fracture_deux_vertebres"] == "Oui":
                    self.listOutput.append(self.Dict_All_Traitements.get("TER"))
                    if self.Patient["age"] <= 70:
                        self.listOutput.append(self.Dict_All_Traitements.get("RAL"))
                    if self.Patient["age"] >= 50 and self.Patient["age"] <= 60:
                        self.listOutput.append(self.Dict_All_Traitements.get("THM"))

            elif self.Patient["fracture_non_severe"] == "Oui" or self.Patient["fracture_non_severe"] == "Non" and self.Patient["fracture_severe"] == "Non":
                self.listOutput.append(self.Dict_All_Traitements.get("ALN"))
                self.listOutput.append(self.Dict_All_Traitements.get("RIS"))
                self.listOutput.append(self.Dict_All_Traitements.get("ZOL"))
                self.listOutput.append(self.Dict_All_Traitements.get("DEN"))

                if self.Patient["age"] <= 70 or self.Patient["z_score_col_femur"] <= 3 and self.Patient["fracture_deux_vertebres"] == "Non":
                    self.listOutput.append(self.Dict_All_Traitements.get("RAL1"))
                if self.Patient["age"] >= 50 and self.Patient["age"] <= 60: # woman
                    self.listOutput.append(self.Dict_All_Traitements.get("THM"))
    
    # cal the class
    def ReturnListTraitments(self):
        unique_items = []
        for item in self.listOutput:
            if item not in unique_items:
                unique_items.append(item)
        
        self.listOutput = unique_items
        if self.Patient["radiotherapie"] == "Oui":
            k = -2
            for item in range(len(self.listOutput)):
                if 'Tériparatide' in self.listOutput[item]:
                    k = item
            if k != -2:
                self.listOutput.pop(k)
        return self.listOutput