
class Calcium(object):
    def __init__(self, Patient):
        self.Patient = Patient
        self.Dictionary_Value_Food_Original = {
            #name : [Calcium unit, unityPatient, total], the idea is to use this dictionary like this [ValueFix, QuantityInsertedByTheUsers, Total]
            # the total is calculated "ValueFix" x "QuantityInsertedByTheUsers"
            "JouLaiVer" : [ 100 , 0 , 0 ],
            "JouLaiBol" : [ 300 , 0 , 0 ],
            "SemLaiVer": [ 14 , 0 , 0 ],
            "SemLaiBol": [ 43 , 0 , 0 ],
            
            "Yaourts" : [ 21 , 0 , 0 ],
            
            "Pots100gr": [ 14 , 0 , 0 ],
            "Pots500gr": [ 68 , 0 , 0 ],
            "Pots1kg" : [ 136 , 0 , 0 ],
            
            "PetModeles": [ 4 , 0 , 0 ],
            "GraModeles" : [ 8 , 0 , 0 ],
            
            "PetFromDur" : [ 19 , 0 , 0 ],
            "MoyFromDur" : [ 38 , 0 , 0 ],
            "GraFromDur" : [ 56 , 0 , 0 ],
            
            "PetFromMol" : [ 9 , 0 , 0 ],
            "MoyFromMol" : [ 17 , 0 , 0 ],
            "GraFromMol" : [ 26 , 0 , 0 ],
            
            "JouPetVian" : [ 8 , 0 , 0 ],
            "JouMoyVian" : [ 15 , 0 , 0 ],
            "JouGraVian" : [ 23 , 0 , 0 ],
            "SemPetVian" : [ 1 , 0 , 0 ],
            "SemMoyVian" : [ 2 , 0 , 0 ],
            "SemGraVian" : [ 3 , 0 , 0 ],
            
            "oeufs" : [ 4 , 0 , 0 ],
            
            "PetPomDeTer" : [ 1 , 0 , 0 ],
            "MoyPomDeTer" : [ 3 , 0 , 0 ],
            "GraPomDeTer" : [ 4 , 0 , 0 ],
            
            "PetFrites" : [ 7 , 0 , 0 ],
            "MoyFrites" : [ 14 , 0 , 0 ],
            "GraFrites" : [ 21 , 0 , 0 ],
            
            "PetSemoule" : [ 1 , 0 , 0 ],
            "MoySemoule" : [ 1 , 0 , 0 ],
            "GraSemoule" : [ 2 , 0 , 0 ],
            
            "PetLegSecs" : [ 4 , 0 , 0 ],
            "MoyLegSecs" : [ 8 , 0 , 0 ],
            "GraLegSecs" : [ 11 , 0 , 0 ],
            
            "PetLegVert" : [ 7 , 0 , 0 ],
            "MoyLegVert" : [ 13 , 0 , 0 ],
            "GraLegVert" : [ 30 , 0 , 0 ],
            
            "Ficelles" : [ 25 , 0 , 0 ],
            "Baguettes" : [ 50 , 0 , 0 ],
            "Biscottes" : [ 4 , 0 , 0 ],
            
            "Fruits" : [ 4 , 0 , 0 ],
            
            "BarChocLait" : [ 6 , 0 , 0 ],
            "TabChocLait" : [ 31 , 0 , 0 ],
            
            "BarChocNoir" : [ 2 , 0 , 0 ],
            "TabChocNoir" : [ 9 , 0 , 0 ],
            
            "VerEauRubinet" : [ 9 , 0 , 0 ],
            "LitEauRubinet" : [ 90 , 0 , 0 ],
                
            "VerEauMinBad" : [ 22 , 0 , 0 ],
            "VerEauMinCon" : [ 46 , 0 , 0 ],
            "VerEauMinEvi" : [ 8 , 0 , 0 ],
            "VerEauMinPer" : [ 14 , 0 , 0 ],
            "VerEauMinVic" : [ 8 , 0 , 0 ],
            "VerEauMinVit" : [ 20 , 0 , 0 ],
            "VerEauMinHep" : [ 55 , 0 , 0 ],
            "VerEauMinAut" : [ 10 , 0 , 0 ],
            
            "LitEauMinBad " : [ 220 , 0 , 0 ],
            "LitEauMinCon" : [ 460 , 0 , 0 ],
            "LitEauMinEvi" : [ 80 , 0 , 0 ],
            "LitEauMinPer" : [ 140 , 0 , 0 ],
            "LitEauMinVic" : [ 80 , 0 , 0 ],
            "LitEauMinVit" : [ 200 , 0 , 0 ],
            "LitEauMinHep" : [ 550 , 0 , 0 ],
            "LitEauMinAut" : [ 100 , 0 , 0 ],
            
            "VerVin" : [ 7 , 0 , 0 ]
        }
        self.TotalCalcium = 0# value of calcium intake from the patient

    def CalculateCalciumIntake(self, Patient):
        self.TotalCalcium = 0

        # set the value inside of the dictionary "QuantityInsertedByTheUsers" depending on the user selection
        self.Dictionary_Value_Food_Original.get("JouLaiVer")[1] = self.Patient["quest1_jour_tasses"]
        self.Dictionary_Value_Food.get("JouLaiBol")[1] = self.Patient["quest1_jour_bols"]
        self.Dictionary_Value_Food.get("SemLaiVer")[1] = self.Patient["quest1_semaine_tasses"]
        self.Dictionary_Value_Food.get("SemLaiBol")[1] = self.Patient["quest1_semaine_bols"]
        
        self.Dictionary_Value_Food.get("Yaourts")[1] = self.Patient["quest2_semaine"]
        
        self.Dictionary_Value_Food.get("Pots100gr")[1] = self.Patient["quest3_100_semaine"]
        self.Dictionary_Value_Food.get("Pots500gr")[1] = self.Patient["quest3_500_semaine"]
        self.Dictionary_Value_Food.get("Pots1kg")[1] = self.Patient["quest3_1000_semaine"]
        
        self.Dictionary_Value_Food.get("PetModeles")[1] = self.Patient["quest4_petit_semaine"]
        self.Dictionary_Value_Food.get("GraModeles")[1] = self.Patient["quest4_grands_semaine"]

        
        if self.Patient["quest5_fromage_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetFromDur")[1] = self.Patient["quest5_fromage_fois_semaine"]
        if self.Patient["quest5_fromage_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyFromDur")[1] = self.Patient["quest5_fromage_fois_semaine"]
        if self.Patient["quest5_fromage_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraFromDur")[1] = self.Patient["quest5_fromage_fois_semaine"]
        
        
        if self.Patient["quest6_fromage_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetFromMol")[1] = self.Patient["quest6_fromage_fois_semaine"]
        if self.Patient["quest6_fromage_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyFromMol")[1] = self.Patient["quest6_fromage_fois_semaine"]
        if self.Patient["quest6_fromage_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraFromMol")[1] = self.Patient["quest6_fromage_fois_semaine"]
        
        
        if self.Patient["quest7_portions_jour"] == "Petites":
            self.Dictionary_Value_Food_Original.get("JouPetVian")[1] = self.Patient["quest7_fois_jour"]
        if self.Patient["quest7_portions_jour"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("JouMoyBian")[1] = self.Patient["quest7_fois_jour"]
        if self.Patient["quest7_portions_jour"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("JouGraVian")[1] = self.Patient["quest7_fois_jour"]
        
        
        if self.Patient["quest7_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("SemPetVian")[1] = self.Patient["quest7_fois_semaine"]
        if self.Patient["quest7_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("SemMoyBian")[1] = self.Patient["quest7_fois_semaine"]
        if self.Patient["quest7_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("SemGraVian")[1] = self.Patient["quest7_fois_semaine"]


        self.Dictionary_Value_Food_Original.get("oeufs")[1] = self.Patient["quest8_semaine"]


        if self.Patient["quest9_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetPomDeTer")[1] = self.Patient["quest9_semaine"]
        if self.Patient["quest9_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyPomDeTer")[1] = self.Patient["quest9_semaine"]
        if self.Patient["quest9_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraPomDeTer")[1] = self.Patient["quest9_semaine"]


        if self.Patient["quest10_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetFrites")[1] = self.Patient["quest10_semaine"]
        if self.Patient["quest10_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyFrites")[1] = self.Patient["quest10_semaine"]
        if self.Patient["quest10_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraFrites")[1] = self.Patient["quest10_semaine"]


        if self.Patient["quest11_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetSemoule")[1] = self.Patient["quest11_semaine"]
        if self.Patient["quest11_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoySemoule")[1] = self.Patient["quest11_semaine"]
        if self.Patient["quest11_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraSemoule")[1] = self.Patient["quest11_semaine"]


        if self.Patient["quest12_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetLegSecs")[1] = self.Patient["quest12_semaine"]
        if self.Patient["quest12_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyLegSecs")[1] = self.Patient["quest12_semaine"]
        if self.Patient["quest12_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraLegSecs")[1] = self.Patient["quest12_semaine"]


        if self.Patient["quest13_portions_semaine"] == "Petites":
            self.Dictionary_Value_Food_Original.get("PetLegVert")[1] = self.Patient["quest13_semaine"]
        if self.Patient["quest13_portions_semaine"] == "Moyennes":
            self.Dictionary_Value_Food_Original.get("MoyLegVert")[1] = self.Patient["quest13_semaine"]
        if self.Patient["quest13_portions_semaine"] == "Grandes":
            self.Dictionary_Value_Food_Original.get("GraLegVert")[1] = self.Patient["quest13_semaine"]


        self.Dictionary_Value_Food_Original.get("Ficelles")[1] = self.Patient["quest14_ficelles_jour"]
        self.Dictionary_Value_Food_Original.get("Baguettes")[1] = self.Patient["quest14_baguettes_jour"]
        self.Dictionary_Value_Food_Original.get("Biscottes")[1] = self.Patient["quest14_biscottes_jour"]


        self.Dictionary_Value_Food_Original.get("Fruits")[1] = self.Patient["quest15_semaine"]


        self.Dictionary_Value_Food_Original.get("BarChocLait")[1] = self.Patient["quest16_barres_semaine"]
        self.Dictionary_Value_Food_Original.get("TabChocLait")[1] = self.Patient["quest16_tablettes_semaine"]


        self.Dictionary_Value_Food_Original.get("BarChocNoir")[1] = self.Patient["quest17_barres_semaine"]
        self.Dictionary_Value_Food_Original.get("TabChocNoir")[1] = self.Patient["quest17_tablettes_semaine"]


        self.Dictionary_Value_Food_Original.get("VerEauRubinet")[1] = self.Patient["quest18_verres_jour"]
        self.Dictionary_Value_Food_Original.get("LitEauRubinet")[1] = self.Patient["quest18_litres_jour"]

    
        if self.Patient["quest19_laquelle"] == "0":
            self.Dictionary_Value_Food.get("VerEauMinBad")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "1":
            self.Dictionary_Value_Food.get("VerEauMinCon")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "2":
            self.Dictionary_Value_Food.get("VerEauMinEvi")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "3":
            self.Dictionary_Value_Food.get("VerEauMinPer")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "4":
            self.Dictionary_Value_Food.get("VerEauMinVic")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "5":
            self.Dictionary_Value_Food.get("VerEauMinVit")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "6":
            self.Dictionary_Value_Food.get("VerEauMinHep")[1] = self.Patient["quest19_verres_jour"]
        if self.Patient["quest19_laquelle"] == "7":
            self.Dictionary_Value_Food.get("VerEauMinAut")[1] = self.Patient["quest19_verres_jour"]


        if self.Patient["quest19_laquelle"] == "0":
            self.Dictionary_Value_Food.get("LitEauMinBad")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "1":
            self.Dictionary_Value_Food.get("LitEauMinCon")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "2":
            self.Dictionary_Value_Food.get("LitEauMinEvi")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "3":
            self.Dictionary_Value_Food.get("LitEauMinPer")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "4":
            self.Dictionary_Value_Food.get("LitEauMinVic")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "5":
            self.Dictionary_Value_Food.get("LitEauMinVit")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "6":
            self.Dictionary_Value_Food.get("LitEauMinHep")[1] = self.Patient["quest19_litres_jour"]
        if self.Patient["quest19_laquelle"] == "7":
            self.Dictionary_Value_Food.get("LitEauMinAut")[1] = self.Patient["quest19_litres_jour"]


        self.Dictionary_Value_Food_Original.get("VerVin")[1] = self.Patient["quest20_chaque_jour"]


        # for each food, now the software calculates "ValueFix" x "QuantityInsertedByTheUsers", only where the user has inserted something
        for i in range (len(self.Dictionary_Value_Food)):
            if self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[1] != "" and self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[1] != 0 :
                self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[2] = int (self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[1]) * int (self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[0]) 

        # now the software sum all the total for all foods
        for i in range (len(self.Dictionary_Value_Food)):
            self.TotalCalcium = self.TotalCalcium + self.Dictionary_Value_Food.get(list(self.Dictionary_Value_Food)[i])[2]


        age = self.Patient["age"]
        if age != 0:
            if age >= 1 and age <= 3:
                self.CalciumIntake = 500
            if age >= 4 and age <= 6:
                self.CalciumIntake = 700
            if age >= 7 and age <=9:
                self.CalciumIntake = 900
            if age >= 10 and age <=18:
                self.CalciumIntake = 1200
            if age >= 19:
                self.CalciumIntake = 900
            if age >= 55 and self.Patient["sexe"] == "Féminin":
                self.CalciumIntake = 1200
            if age >- 65 and self.Patient["sexe"] == "Masculin":
                self.CalciumIntake = 1200
        else:
            pass

        
        self.Patient["apport_calcium"] = self.TotalCalcium
        self.Patient["calcium_intake"] = self.CalciumIntake

        self.CalciumVar = f"{self.TotalCalcium} / {self.CalciumIntake} mg/jour"