from pathlib import Path
# Remplacé l'importation de docxtpl par une classe fictive pour contourner le problème de dépendance
# from docxtpl import RichText
class RichText:
    """Classe fictive pour remplacer RichText de docxtpl"""
    def __init__(self, *args, **kwargs):
        self.text = ""

    def add(self, text):
        self.text += text


    def __str__(self):
        return self.text

from datetime import datetime


from apoteose.patients.classes.Traitements import Traitements
from apoteose.patients.classes.DecisionTree import DecisionTree

class DiagnoseAnalysis:
    def __init__(self, arg):
        self.Patient = arg
        self.TreatmentContext = {}
        self.setTreatmentContext()
        self.Patient["IMClow"] = "Oui" if float(self.Patient["imc"]) < 18 else "Non"
        self.DT = DecisionTree().DecisionChoice(self.Patient)
        self.Review = RichText()
        self.ListOfReview = ["+ Actualisation 2018 des recommandations françaises du traitement de l'ostéoporose post-ménopausique",
                    "+ Recommandations françaises de stratégies thérapeutiques pour la prévention et le traitement de l'ostéoporose induite par les traitements adjuvants du cancer du sein",
                    "+ Recommandations françaises de stratégies thérapeutiques pour la prévention et le traitement de l'ostéoporose induite par la castration dans le cancer de la prostate",
                    "+ Actualisation 2014 des recommandations sur la prévention et le traitement de l'ostéoporose cortico-induite",
                    "+ Recommandations françaises de la prise en charge et du traitement de l'De masculine",
                    "+ Selon le Protocole National de Diagnostic et de Soins 2019 PNDS"     # this is for the densitometrie pediatrique
                    ]

        self.Dictionary_possible_antecedents = {
            'edocrinopathie': 'endocrinopathie',
            'hyperparathyroide': 'Hyperparathyroïde',
            'hyperthyroide': 'Hyperthyroïde',
            'hypercorticisme': 'Hypercorticisme',
            'insuffisance_hypophysaire':
            'Insuffisance hypophysaire',
            'hypogonadisme': 'Hypogonadisme',
            'diabete_type': 'Diabete type 1 et 2',
            'anorexie_mentale': 'Anorexie Mentale',

            #Rhumatisme Inflammatoire Chronique
            'rhumatisme_inflammatoire': 'RhumatismeInflammatoireChronique',
            'polyarthrite_rheumatoide': 'Polyarthrite rheumatoïde',
            'spondylarthrite': 'Spondylarthrite',
            'rhumatisme_psoriasique': 'Rhumatisme psoriasique',
            'lupus': 'Lupus érythémateux systémique',
            'autres_connectivites': 'Autres connectivites',

            #Maladie Genetique
            'maladie_genetique': 'MaladieGenetique',
            'hemochromatose': 'Hémochromatose',
            'mastocytose': 'Mastocytose',
            'drepanocytose': 'Drépanocytose',

            #pathologie intestinale/digestive
            'pathologie_intestinale': 'pathologieintestinale/digestive',
            'maladie_crohn': 'Maladie de Crohn',
            'maladie_coeliaque': 'Maladie coeliaque',
            'bypass': 'ByPass',
            'hepatopathie_chronique': 'Hepatopathie chronique',
            'rectocolite_ulcero': 'Rectocolite ulcéro-hémorragique',


            #Insuffisance rénale chronique
            'insuffisance_renale': 'Insuffisance rénale chronique',
            'clairance_inferieure_30': 'Clairance inférieure à 30 ml/mn'
            }

        self.Dictionary_Traitement = {
            "traitement_subs_menopause": ["Traitement substitutif de la ménopause", "traitement_subs_menopause_init_date", "traitement_subs_menopause_end_date"] ,
            "traitement_denosumab": ["Traitement par Dénosumab", "traitement_denosumab_init_date", "traitement_denosumab_end_date"] ,
            "traitement_teriparatide": ["Traitement par Tériparatide", "traitement_teriparatide_init_date", "traitement_teriparatide_end_date"] ,
            "traitement_raloxifene": ["Traitement par Raloxifene", "traitement_raloxifene_init_date", "traitement_raloxifene_end_date"] ,
            "traitement_risedronate": ["Risedronate", "traitement_risedronate_init_date", "traitement_risedronate_end_date"] ,
            "traitement_aledronate": ["Aledronate", "traitement_aledronate_init_date", "traitement_aledronate_end_date"] ,
            "traitement_acide_zoledronique": ["Acide Zoledronique", "traitement_acide_zoledronique_init_date", "traitement_acide_zoledronique_end_date"] ,
        }

        self.Dictionary_Traitement_Basics = {
            "supplem_calcium": "Supplementation en calcium" ,
            "vitamine_d": "Supplementation en vitamine D",
            "traitement_bisphosphonates": "Traitement par bisphosphonates",
            "traitement_osteo": "Traitement spécifique actuel de l'ostéoporose"
        }

        self.context = {
            "Prenom": self.Patient["prenom"],
            "Nom": self.Patient["nom"],
            "Age": self.Patient["age"],
            "Taille": self.Patient["taille"],
            "Poids": self.Patient["poids"],
            "Date_de_Naissance": self.Patient["date_naissance"],
            "IMC": self.Patient["imc"],
            "Sexe": self.Patient["sexe"],
            "FirstSection": f"Patient de sexe {self.Patient['sexe']} de {self.Patient['age']} ans",
            "Tabagisme": "" if self.Patient["tabagisme"] == "Oui" else "Non ",
            "Alcool": "" if self.Patient["alcool"] == "Oui" else "Pas de ",
            "Activ": "" if self.Patient["activite_phsique"] == "Oui" else "Pas d'",
            "VitD": "" if self.Patient["vitamine_d"] == "Oui" else "Pas de ",
            "Plus": "",
            "Frac": "",
            "Calc": "",
            "Pare": "" if self.Patient["fracture_fragilite_femoral"] == "Oui" else "Pas de ",
            "Chut": "" if self.Patient["chutes_frequentes"] == "Oui" else "Pas de ",
            "PathAsso": "",
            "Inducteurs": "",
            "NoInduct": "",
            "Information": self.Patient["information_complementaires"],
            "Score": "Z Score" if self.Patient["age"] <= 24 else "T Score",
            "created_at": datetime.utcnow(),
            "Path": self.DT,
            "Femur": self.Patient["z_score_col_femur"],
            "FemurClass": self.Classification(self.Patient["z_score_col_femur"]),
            "Hanche": self.Patient["z_score_hache"],
            "HancheClass": self.Classification(self.Patient["z_score_hache"]),
            "Ranchis": self.Patient["z_score_rachis"],
            "RanchisClass": self.Classification(self.Patient["z_score_rachis"]),
            "Radius": 1 if self.Patient["z_score_extremite_popup"] == True else 0,
        }

        ########### FirstSection, description patient
        if self.Patient["menopause"] == "Oui":
            if self.Patient["menopause_age"] <= 40:
                self.context["FirstSection"] += f", ménopause précose à l'âge de {self.Patient['menopause_age']} ans."
            else:
                self.context["FirstSection"] += f", ménopause précose à l'âge de {self.Patient['menopause_age']} ans."
        elif self.Patient["age"] <= 24:
            pass
        else:
            self.context["FirstSection"] += ", non ménopause."


        if self.Patient["IMClow"] == "Yes":
            if self.Patient["sexe"] == "Masculin":
                self.context["FirstSection"] += " Le patient a un IMC faible."
            else:
                self.context["FirstSection"] += " La patiente a un IMC faible."

        if self.Patient["supplem_calcium"] == "Oui":
            self.context["Calc"] += f"\nSupplémentation calcique de {0 if self.Patient['dose_calcium_journaliere'] == None else self.Patient['dose_calcium_journaliere']} mg/jour"
        #elif self.Patient["apport_calcium"] != 0:
            #self.context["Calc"] += f"\nApport calcique journalier = " + str(self.Patient['apport_calcium']) + "mg/jour",

        ########### Antecedent de Fracture de Faible Energie
        if self.Patient["antecedent_fracture_faible_energie"] == "Oui":
            if self.Patient["fracture_severe"] == "Oui":
                self.context["Plus"] += "\n\tFracture sévère"
                if self.Patient["fracture_deux_vertebres"] == "Oui":
                    self.context["Plus"] += "\n\tFracture de plus de 2 vertébres"
            if self.Patient["fracture_non_severe"] == "Oui":
                self.context["Plus"] += "\nFracture non sévère"
        else:
            self.context["Frac"] = "Pas d'"


        ########### Pathologie Associées
        self.antecedentes = ["edocrinopathie", "rhumatisme_inflammatoire", "maladie_genetique", "pathologie_intestinale"]
        self.EnterPathAssoc = False

        for pathologie in self.Dictionary_possible_antecedents:
           if self.Patient[pathologie] == "Oui":
               self.context["PathAsso"] += f"{self.Dictionary_possible_antecedents[pathologie]}\n"
               if pathologie in self.antecedentes:
                   self.EnterPathAssoc = True

        self.context["NoYesPath"] = "Pas d'antécédent pathologique notable" if self.EnterPathAssoc == False else "Pathologies associées"


        ########### Autres traitements inducteurs de l'osteoporose
        self.Inducteurs = ""

        if self.Patient["tamoxifene"] == "Oui" or self.Patient["hormonotherapie"] == "Tamoxifène":
            self.Inducteurs += "Tamoxifène"
        if self.Patient["analogue_lh_rh"] == "Oui":
            self.Inducteurs += "\nAnalogue de LH-RH"
        if self.Patient["horm_anastrazole"] == "Oui":
            self.Inducteurs += "\nHorm Anastrazole"
        if self.Patient["horm_letrozole"] == "Oui":
            self.Inducteurs += "\nHorm Letrozole"
        if self.Patient["horm_exemestane"] == "Oui":
            self.Inducteurs += "\nHorm Exemestane"
        if self.Patient["traitement_vih"] == "Oui":
            self.Inducteurs += "\nInhibiteur de a protéase du VIH"

        if self.Inducteurs == "":
            self.context["NoInduct"] = "Pas d'"

        self.context["Inducteurs"] = self.Inducteurs


        ########### Traitement spécifique de l'ostéoporose
        self.TraitementPasse = ""
        self.DatesTraitement = [""]

        for traitement in list(self.Dictionary_Traitement.keys())[:4]:
            if self.Patient[traitement] == "Oui":
                self.TraitementPasse += f"\n{self.Dictionary_Traitement[traitement][0]}\t debut en {self.Patient[self.Dictionary_Traitement[traitement][1]]}\t\t fin en {self.Patient[self.Dictionary_Traitement[traitement[2]]]}"

        if self.Patient["traitement_bisphosphonates"] == "Oui":
            self.TraitementPasse += "\nTraitement par bisphosphonates"
            for traitement in list(self.Dictionary_Traitement.keys())[4:7]:
                self.TraitementPasse += f"\n{self.Dictionary_Traitement[traitement][0]}\t debut en {self.Patient[self.Dictionary_Traitement[traitement][1]]:%m/%Y}\t\t fin en {self.Patient[self.Dictionary_Traitement[traitement[2]]]:%m/%Y}"

        if self.TraitementPasse == "":
            self.context["NoTraitSpe"] = "Pas de prise d'un "

        self.context["TraiSpe"] = self.TraitementPasse


        ########### Corticotherapie
        self.context["Cortico"] = ""

        if self.Patient["corticotherapie_plus_3"] == "Oui":
            self.context["Cortico"] = ""
            if self.Patient["corticotherapie_plus_7_5"] == "Oui":
                self.context["PlusDe"] = "\n\t Plus de 7.5 mg/jour"
            else:
                self.context["PlusDe"] = "\n\t Moins de 7.5 mg/jour"
        else:
            self.context["Cortico"] = "Pas de "


        ########### FRAX
        self.context["Frax"] = f"{self.Patient['frax']}%"
        try:
            if self.Patient["frax_cancer"] != "":
                self.Patient["Frax"] += f"\n FRAX Fracture de Hanche: {self.Patient['frax_cancer']}"
        except:
            pass


        ########### Information d'examen
        # if self.Patient["z_score_femur_popup"] == True:
        #     self.context["Femur"] = str(self.Patient["z_score_col_femur"])
        #     self.context["FemurClass"] = self.Classification(self.Patient["z_score_col_femur"])
        # else:
        #     self.context["Femur"] = "-"
        #     self.context["FemurClass"] = "-"

        # if self.Patient["z_score_hanche_popup"] == True:
        #     self.context["Hanche"] = self.Patient["z_score_hache"]
        #     self.context["HancheClass"] = self.Classification(self.Patient["z_score_hache"])
        # else:
        #     self.context["Hanche"] = "-"
        #     self.context["HancheClass"] = "-"

        # if self.Patient["z_score_rachis_popup"] == True:
        #     self.context["Rachis"] = self.Patient["z_score_rachis"]
        #     self.context["RachisClass"] = self.Classification(self.Patient["z_score_rachis"])
        # else:
        #     self.context["Rachis"] = "-"
        #     self.context["RachisClass"] = "-"

        if self.Patient["z_score_extremite_distale"] == "Oui":
            self.radius = 1 if self.Patient["z_score_extremite_popup"] == True else 0
            self.context["Radius"] = self.radius
            self.context["RadiusClass"] = self.Classification(self.radius)
        else:
            self.context["Radius"] = "-"
            self.context["RadiusClass"] = "-"


        ########### Diagnose Patient
        if self.DT[0] == True:

            if self.Patient["age"] <= 24:
                self.context["Diagnose"] = "Fragilité osseuse"
            else:
                self.context["Diagnose"] = "Traitement anti-ostéoporotique recommandé"

                if self.Patient["sexe"] == "Masculin":
                    self.context["InfoTrait"] = """
Un bilan diagnostique et pré-thérapeutique est indiqué par la réalisation d'une
Numération Formule Sanguine, VS,CRP, Calcémie, Albuminémie, Phosphorémie, Phosphatases alcalines, Electrophorèse des protides, Créatininémie, Transaminases, Gamma GT, Testostérone totale et dosage de la 25OH Vitamine D
                    """
                else:
                    self.context["InfoTrait"] = """
Un bilan diagnostique et pré-thérapeutique est indiqué par la réalisation d'une
Numération Formule Sanguine, VS, CRP, Calcémie, Albuminémie, Phosphorémie, Phosphatases alcalines, Electrophorèse des protides, Créatininémie, TSH, PTH et dosage de la 25OH Vitamine D
                    """
        else:
            if self.Patient["age"] <= 24:
                self.context["Diagnose"] = "Pas de Fragilité osseuse"
            else:
                self.context["Diagnose"] = "Traitement anti-ostéoporotique non racommandé"

        # there is just one condition where I have to print the examn necessary when it's non menopause and T score inferior a -2.5
        if self.DT[0] == False and self.Patient["age"] == "Feminin" and self.Patient["menopause"] == "Non" and DecisionTree.DecisionChoice.lowestZScore(self.Patient) < -2.5:
            self.context["InfoTrait"] = """
Un bilan diagnostique et pré-thérapeutique est indiqué par la réalisation d'une
Numération Formule Sanguine, VS, CRP, Calcémie, Albuminémie, Phosphorémie, Phosphatases alcalines, Electrophorèse des protides, Créatininémie, TSH, PTH et dosage de la 25OH Vitamine D
            """

        # independent of the result True/False we want to add the situation
        if self.Patient["hyperparathyroide"] == "Oui":
            TScoreMin = DecisionTree.DecisionChoice.lowestZScore(self.Patient)
            LabelAdd = ""
            if TScoreMin >= -1:
                LabelAdd = "un T score superieur à -1: la densitométrie osseuse normale."
            elif TScoreMin <= -2.5:
                LabelAdd = "un T score inferieur à -2.5: la densitométrie osseuse en faveur d'une ostéoporose."
            else:
                LabelAdd = "un T score entre -1 et -2.5: la densitométrie osseuse en faveur d'une ostéopénie."

            self.context["Hyperpa"] = """\nLe patient(e) est hyperparathyroïdique et a {}""".format(LabelAdd)

        self.context["PathDiagnose"] = self.DT


        # printing the traitement, these are the output of the Decision Tree
        All = ""

        for i in range(len(Traitements(self.Patient).ReturnListTraitments())):
            Traitment = "◦ "
            print(Traitements(self.Patient).ReturnListTraitments()[i])

            Traitment += str(Traitements(self.Patient).ReturnListTraitments()[i]) + " "
            All += Traitment + "\n"
            self.context["Traitement"] = All

        if self.DT[0] == True and self.Patient["age"] >= 25:
            self.context["PhraseTraitement"] = "Durée proposée de la séquence thérapeutique "


        ########### Traitement Patient
        self.context["AdviseGeneral"] = ""
        self.context["Advise"] = ""
        self.context["PossibleVitD"] = ""
        self.context["DiagnoseCalcium"] = ""
        typePatient = ""
        antecedent = ""
        EnterEvaluationMorphologi = False

        self.context["Advise"] = "- Maintien d'une activité physique réguilère, 30 min/jour"
        if self.Patient["tabagisme"] == "Oui":
            self.context["Advise"] = self.context['Advise'] + "\n- Sevrage du tabac"
        if self.Patient["alcool"] == "Oui":
            self.context["Advise"] = self.context["Advise"] + "\n- Diminution de la consommation d'alcool"
        if self.Patient["corticotherapie"] == "Oui" or self.Patient["cancer_sein"] == "Oui" and self.Patient["age"] >= 24:
            self.context["Advise"] = self.context["Advise"] + "\n- Utilisation de la dose minimale efficace de glucorticoides"
        if self.Patient["age"] <= 24:
            self.context["Advise = "] = self.context["Advise"] + "\n- Recherche de la dose de corticoïdes minimale efficace" + "\n- Assurer un état nutritionnel satisfaisant"
            self.context["Advise"] += "\n- Contrôle de la maladie causale" + "\n- Traiter un déficit hormonal"

        #it's necessary for implementing the next for the printing, be careful because it's important the order
        if self.Patient["cancer_prostate"] == "Oui":
            typePatient = ""
            antecedent = ""
            EnterEvaluationMorphologi = True

        if self.Patient["menopause"] == "Oui":
            typePatient +=  "chez la femme ménopausée, "
            antecedent = """
\t+ antécédent de fracture vertébrale et maladies chroniques et traitements (corticothérapie, inhibiteurs de
\t  l'aromatase) avec risque important de fracture vertébrale
"""
            EnterEvaluationMorphologi = True

        if self.Patient["cancer_sein"] == "Oui":
            typePatient = "chez une patiente avec cancer du sein"
            antecedent = """
\t+ antécédent de fracture vertébrale et maladies chroniques et traitements (corticothérapie, inhibiteurs de
\t  l'aromatase) avec risque important de fracture vertébrale
            """
            EnterEvaluationMorphologi = True

        if self.Patient["corticotherapie"] == "Oui":
            typePatient += "chez un patient avec corticothérapies, "
            antecedent = """
\t+ antécédent de fracture vertébrale et maladies chroniques et traitements (corticothérapie, inhibiteurs de
\t  l'aromatase) avec risque important de fracture vertébrale
            """
            EnterEvaluationMorphologi = True

        LostOfHeight = -100
        PrintEvaluationMorphologique = False
        try:
            LostOfHeight = (self.Patient["taille_20"] - self.Patient["taille"])
            if LostOfHeight >= 4:
                PrintEvaluationMorphologique = True
        except:
            pass

        if self.Patient["corticotherapie"] == "Oui":
            PrintEvaluationMorphologique = True
        if self.Patient["sexe"] == "Feminin":
            if self.Patient["horm_anastrazole"] == "Oui" or self.Patient["horm_letrozole"] == "Oui" or self.Patient["horm_exemestane"] == "Oui":
                PrintEvaluationMorphologique = True
            if self.Patient["fracture_deux_vertebres"] == "Oui":
                PrintEvaluationMorphologique = True

        if EnterEvaluationMorphologi == True and PrintEvaluationMorphologique == True and self.Patient["age"] >= 25:
            self.context["Advise"] += f"""
- Une évaluation morphologique à la recherche de fractures vertébrales par radiographies standards du rachis dorsolombaire est indiquée {typePatient} en cas de rachialgies ou si un des critères suivants est présent :
\t+ perte de taille ≥ 4 cm (mesure de la taille comparée à la taille rapportée à l'âge de 20 ans)
\t+ perte de taille prospective ≥ 2 cm, {antecedent}.
        """

        if self.Patient["age"] >= 25:
            self.context["Advise"] += """
- L'éviction des facteurs de risque de fractures et de chutes est nécessaire: sevrage des médicaments non indispensables (opiacés, hypnotiques...)
        """

        else:
            self.context["AdviseGeneral"] = "Recommandations sur les mesures générales préventives:"
            pathDoc= "file:///" + str( Path(__file__).parent / "official/pnds_fragilites_osseuses_Pediatrique-27-09-2019.pdf")
            self.Review.add("\n" + self.ListOfReview[5])

            self.context["Advise"] += """
- Bisphosphonates par voie IV (pamidronate ou zoledronate) indiqués si fragilité osseuse symptomatique selon définition (fracture vertébrale et/ou fractures des os longs cliniquement significatives et DMO mineur de -2 Z-score) ou si douleurs osseuses chroniques et DMO mineur de -2 Z-score
- La posologie et la durée du traitement est à discuter entre les médecins référents de la pathologie et les médecins experts de la santé osseuse
- Bisphosphonates non indiqués si DMO basse isolée (sans fractures), à discuter au cas par cas dans des centres spécialisés
            """

        if self.Patient["sexe"] == "Masculin" and self.Patient["age"] >= 25:
            self.context["Advise"] += "\n- L'apport alimentaire quotidien recommandé en protéines est de 1 gramme/Kg de poids corporel."

        if self.Patient["age"] <= 24:
            self.context["PossibleVitD"] = """
- Assurer des apports calciques et en vitamine D optimaux: Taux de 25OHD au minimum majeur de 20 ng/ml et de façon optimale majeur de 30 ng/ml associé à un apport de calcium quotidien correspondant aux apports recommandés pour l'âge.
            """

        else:
            self.context["PossibleVitD"] = "- La concetration recommandée actuellement de 25 OH vitamine D est d'au moins 30 ng/mL (75nmol/L)."
            if self.Patient["cancer_prostate"] == "Oui":
                self.context["PossibleVitD"] += " Un dosage annuel de la 25OH vitamine D est recommandé."

        ## Change this to add the total calcium from calcium classes
        if self.Patient["apport_calcium"] == 500:
            CalciumEnough = 0
        elif self.Patient["apport_calcium"] == 700:
            CalciumEnough = 0
        elif self.Patient["apport_calcium"] == 900:
            CalciumEnough = 0
        elif self.Patient["apport_calcium"] == 1200:
            CalciumEnough = 0
        else:
            CalciumEnough = 1

        if CalciumEnough == 0 and self.Patient["hyperparathyroide"] == "Oui":
            self.context["DiagnoseCalcium"] += "Apport alimentaire insuffisant en calcium mais il ne peux pas posible parce que il y a Hyperparathyroïde"

        if self.Patient["menopause"] == "Oui":
            add = " chez les femmes ménopausées âgées de plus de 50 ans"
        else:
            add = ""

        if self.Patient["age"] >= 25:
            self.context["DiagnoseCalcium"] += f"""
- Les apports en calcium quotidiens recommandés doivent être d'au moins 1 gr à 1.2 gr{add}. En privilégiant les apports alimentaires.
- Pour couvrir ces besoins, il faut consommer 4 produits laitiers par jour (yaourts, fromage frais, laits fermentés, fromages, lait...).
            """


        ######### Sequence Therapeutique
        self.context["AdviseTrai"] = ""
        self.context["Control"] = ""

        ### Cancer du sein and not pediatrique
        if self.Patient["cancer_sein"] == "Oui" and self.Patient["age"] >= 25:
            self.context["AdviseGeneral"] = "\nMesures générales indiquées chez toutes patientes sous traitements adjuvants du cancer du sein"
            pathDoc= "file:///" + str( Path(__file__).parent / "official/reco-sein%20ostéoporose.pdf")
            self.Review.add( "\n" + self.ListOfReview[1])

            if self.DT[0] == True:
                self.textCancDuSein = """
--- Cancer du sein ---
- Une évaluation entre 2 et 3 ans doit être réalisée et la poursuite du traitement discutée en fonction des résultats obtenus à la fin de cette première séquence.
- La réalisation d'une mesure de la DMO est recommandée enfin de séquence thérapeutique.
                """
                self.context["AdviseTrai"] += self.textCancDuSein

            else:
                if DecisionTree.DecisionChoice.lowestZScore(self.Patient) >= -1:
                    self.textCancDuSein = f"""Un contrôle densitométrique est indiqué dans 18 à 24 mois."""
                    self.context["Control"] += self.textCancDuSein

        ########## Cancer du Prostate, and not pediatrique
        if self.Patient["cancer_prostate"] and self.Patient["age"] >= 25:
            self.context["AdviseGeneral"] = "\nMesures générales indiquées chez tous les patients ayant subi la castration dans le cancer de la prostate"
            pathDoc= "file:///" + str( Path(__file__).parent / "official/reco-prostate%20ostéoporose.pdf")
            self.Review.add( "\n" + self.ListOfReview[2])

            if self.DT[0] == True:
                self.textCancDuProstate = """
--- Cancer du prostate ---
- Un traitement d'une durée initiale de 3 à 5 ans est proposé avec une réévaluation du risque en fin de première séquence.
- La réalisation d'une mesure de la DMO est recommandée enfin de séquence thérapeutique.
                """
                self.context["AdviseTrai"] += self.textCancDuProstate

            else:
                self.textCancDuProstate = f"Un contrôle densitométrique est indiqué dans 12 à 24 mois."
                self.context["Control"] += self.textCancDuProstate

        ######### Corticotherapie not pediatrique
        if self.Patient["corticotherapie"] == "Oui" and self.Patient["age"] >= 25:
            self.context["AdviseGeneral"] = "\nMesures générales indiquées chez tous patients sous corticoides au long cours"
            pathDoc= "file:///" + str( Path(__file__).parent / "official/OSTEOPOROSE%20CORTISONIQUE.pdf")
            self.Review.add( "\n" + self.ListOfReview[3])
            if self.DT[0] == True:
                self.textCorti = """
--- Corticotherapie ---
- L'expérience clinique de l'utilisation des traitements dans l'ostéoporose cortisonique est de deux ans pour les bisphosphonates et de 36 mois pour le Tériparatide (remboursement limité à une prescription de 18 mois et AMM limité à 24 mois)
- Ce sont les durées au terme desquelles se discute la poursuite ou l'arrêt du traitement en fonction du risque fracturaire résiduel.
- La réalisation d'une mesure de la DMO est recommandée enfin de séquence thérapeutique.
                """
                self.context["AdviseTrai"] += self.textCorti
            else:
                self.textCorti = "Un contrôle densitométrique est indiqué dans 1 an"
                self.context["Control"] += self.textCorti

        ######### Man, and not pediatrique, and not orticotherapie, and not cancer du prostate
        if self.Patient["sexe"] == "Masculin" and self.Patient["age"] >= 25 and self.Patient["cancer_prostate"] == "Oui":
            self.context["AdviseGeneral"] = "\nMesures générales indiquées chez tous les patients masculine"
            if self.DT[0] == True:
                self.textMan = f"""
--- Homme ---
- Un traitement d'une durée initiale de 3 ans est proposé avec une réévaluation du risque en fin de première séquence.
- La réalisation d'une mesure de la DMO est recommandée enfin de séquence thérapeutique.
                """
                self.context["AdviseTrai"] += self.textMan

        ########### Woman, not pediatrique, not corticotherapie, not cancer du sein
        if self.Patient["sexe"] == "Feminin" and self.Patient["age"] >= 25 and self.Patient["corticotherapie"] == "Non" and self.Patient["cancer_sein"] == "Non":
            if self.Patient["menopause"] == "Oui":
                self.context["AdviseGeneral"] = "\nMesures générales indiquées chez toutes les femmes ménopausées même s'il n y'a pas d'indication à un traitement spécifique"
            else:
                self.context["AdviseGeneral"] = "\nMesures générales indiquées chez toutes les femmes NON ménopausées même s'il n y'a pas d'indication à un traitement spécifique"

            if self.DT[0] == True: #treatment only because is woman
            #first situation
                self.textWomanMeno = f"""
--- Woman menopause ---
- Les traitements ont fait la preuve de leur efficacité anti-fracturaire dans des études contrôlées de 18 mois pour le tériparatide, de 3 ans pour l'acide zolédronique et le dénosumab et de 5 ans pour les autres traitements.
- Ce sont les durées au terme desquelles se discute la poursuite ou l'arrêt du traitement en fonction du risque fracturaire résiduel.
- Une mesure de la DMO peut être réalisée dans les 2 à 3 ans après le début du traitement et à chaque fois qu'est envisagée une modification du traitement
                """
                self.context["AdviseTrai"] += self.textWomanMeno

        self.context["ListOfReview"] = self.Review


    def Classification(self, TValue):
        """
        Classification selon les normes internationales de l'OMS :
        - T-Score ≤ -2.5 : Ostéoporose
        - T-Score entre -1 et -2.5 : Ostéopénie
        - T-Score > -1 : Normal
        Pour les patients < 24 ans, utilise le Z-Score
        """
        if self.Patient["age"] <= 24:
            # Utilisation du Z-Score pour les patients pédiatriques
            if TValue <= -2.0:
                return "Fragilité osseuse significative"
            elif -2.0 < TValue <= -1.0:
                return "Fragilité osseuse modérée"
            else:
                return "Densité osseuse normale"
        else:
            # Utilisation du T-Score pour les adultes
            if TValue <= -2.5:
                if self.Patient["fracture_severe"] == "Oui":
                    return "Ostéoporose sévère avec fracture"
                return "Ostéoporose"
            elif -2.5 < TValue <= -1.0:
                return "Ostéopénie"
            else:
                return "Densité osseuse normale"

    def setTreatmentContext(self):
        """
        Définit le contexte des traitements et facteurs de risque
        selon les recommandations internationales
        """
        # Traitements inducteurs d'ostéoporose
        self.TreatmentContext["bisphosphonates"] = {
            "name": "Bisphosphonates",
            "indication": "Traitement de première intention de l'ostéoporose",
            "contre_indications": [
                "Insuffisance rénale sévère (DFG < 30 ml/min)",
                "Hypocalcémie",
                "Grossesse"
            ],
            "surveillance": [
                "Densitométrie osseuse annuelle",
                "Bilan phosphocalcique semestriel",
                "Suivi dentaire régulier"
            ]
        }

        # Facteurs de risque majeurs
        self.TreatmentContext["risk_factors"] = {
            "majeurs": [
                "Âge > 65 ans",
                "Antécédent de fracture de fragilité",
                "IMC < 19 kg/m²",
                "Corticothérapie > 3 mois",
                "Ménopause précoce (< 40 ans)"
            ],
            "mineurs": [
                "Tabagisme",
                "Sédentarité",
                "Déficit en vitamine D",
                "Consommation excessive d'alcool"
            ]
        }

        # Recommandations selon le profil
        self.TreatmentContext["recommendations"] = {
            "générales": [
                "Apport calcique de 1200 mg/jour",
                "Supplémentation en vitamine D (800-1000 UI/jour)",
                "Activité physique régulière avec impact",
                "Arrêt du tabac et limitation de l'alcool"
            ],
            "spécifiques": []
        }

        # Adaptation selon le profil du patient
        if self.Patient["age"] > 65:
            self.TreatmentContext["recommendations"]["spécifiques"].append(
                "Évaluation du risque de chute et aménagement du domicile"
            )

        if self.Patient["fracture_severe"] == "Oui":
            self.TreatmentContext["recommendations"]["spécifiques"].append(
                "Traitement anti-ostéoporotique de première intention"
            )

    def check_missing_data(self):
        """
        Vérifie les données manquantes et retourne un diagnostic partiel si nécessaire
        """
        missing_data = []
        required_fields = [
            "age", "sexe", "imc", "t_score", "z_score",
            "fracture_severe", "menopause", "corticotherapie"
        ]

        for field in required_fields:
            if field not in self.Patient or self.Patient[field] is None:
                missing_data.append(field)

        return missing_data

    def generate_diagnosis_data(self):
        """
        Génère les données structurées pour le diagnostic
        """
        missing_data = self.check_missing_data()
        diagnosis_data = {
            "t_score": self.Patient.get("t_score", "Non disponible"),
            "z_score": self.Patient.get("z_score", "Non disponible"),
            "t_score_class": self.Classification(self.Patient.get("t_score", 0)),
            "z_score_class": self.Classification(self.Patient.get("z_score", 0)),
            "risk_factors": self.TreatmentContext["risk_factors"],
            "recommendations": self.TreatmentContext["recommendations"],
            "missing_data": missing_data
        }

        # Détermination du diagnostic final
        if missing_data:
            diagnosis_data["final_diagnosis"] = "Diagnostic partiel - Données manquantes"
        else:
            diagnosis_data["final_diagnosis"] = self.Classification(
                self.Patient.get("t_score", 0)
            )

        return diagnosis_data

    def generate_report(self, output_path):
        """
        Génère un rapport PDF complet
        """
        from .ReportGenerator import ReportGenerator

        diagnosis_data = self.generate_diagnosis_data()
        report_generator = ReportGenerator(self.Patient, diagnosis_data)
        report_generator.generate_report(output_path)

        return diagnosis_data

