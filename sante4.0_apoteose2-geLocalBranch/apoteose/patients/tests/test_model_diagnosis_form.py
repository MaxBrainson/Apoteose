from datetime import datetime
from django.test import TestCase

from apoteose.patients.models import Diagnosis


class DiagnosisModelTest(TestCase):
    def setUp(self):
        self.obj = Diagnosis(
            prenom = 'Geovana', 
            nom = 'Sousa', 
            date_naissance = '2000-07-19', 
            age = '22', 
            sexe = 'Féminin', 
            menopause = 'Non',
            menopause_age = None,
            taille = '165', 
            taille_20 = '165', 
            poids = '65', 
            imc = '23.89',

            vitamine_d = 'Non', 
            supplem_calcium = 'Non', 
            dose_calcium_journaliere = '1200', 
            traitement_osteo = 'Non', 
            traitement_subs_menopause = 'Non',  
            traitement_menopause_init_date = None,  
            traitement_menopause_end_date = None,  
            traitement_raloxifene = 'Non', 
            traitement_raloxifene_init_date = None, 
            traitement_raloxifene_end_date = None, 
            traitement_bisphosphonates = "Non",
            traitement_risedronate = "Non",
            traitement_risedronate_init_date = None,
            traitement_risedronate_end_date = None,
            traitement_aledronate = 'Non',
            traitement_aledronate_init_date = None,
            traitement_aledronate_end_date = None,
            traitement_acide_zoledronique = "Non",
            traitement_acide_zoledronique_init_date = None,
            traitement_acide_zoledronique_end_date = None,
            traitement_denosumab = 'Non', 
            traitement_denosumab_init_date = None, 
            traitement_denosumab_end_date = None, 
            traitement_teriparatide ='Non', 
            traitement_teriparatide_init_date =None, 
            traitement_teriparatide_end_date =None, 
            bonne_observance = 'Non', 
            traitement_bonne_init_date = None, 
            traitement_bonne_end_date = None, 

            apport_calcium = '1200',

            z_score_col_femur = '1', 
            z_score_hache = '-1', 
            z_score_rachis = '2', 
            z_score_extremite_distale = 'Non', 
            frax = '45', 
            z_score_femur_popup = 'Non', 
            z_score_hanche_popup = 'Non', 
            z_score_rachis_popup = 'Non', 
            z_score_extremite_popup = 'Non', 

            tabagisme = 'Non', 
            alcool = 'Non', 
            activite_phsique = 'Non', 
            chutes_frequentes = 'Non', 
            traitement_vih = 'Non', 
            corticotherapie = 'Non', 
            corticotherapie_plus_3 = 'Non',  
            corticotherapie_plus_7_5 = 'Non', 
            hormonotherapie = 'Non', 
            hormonotherapie_choices = 'Décapeptyl', 

            radiotherapie = 'Non', 
            cancer_prostate = 'Non', 
            cancer_sein = 'Non', 
            comorbites_associees = 'Non', 
            castraction_chirurgiale = 'Non', 
            frax_cancer = '0', 

            analogue_lh_rh = 'Non',
            tamoxifene = 'Non',
            horm_anastrazole = 'Non',
            horm_letrozole = 'Non',
            horm_exemestane = 'Non',
            amenorrhee_induite = 'Non',

            antecedent_fracture_faible_energie = 'Non', 
            fracture_severe =  'Non', 
            fracture_deux_vertebres = 'Non',  
            fracture_non_severe = 'Non', 
            fracture_fragilite_femoral = 'Non',  

            edocrinopathie = 'Non',
            hyperparathyroide = 'Non', 
            hyperthyroide = 'Non', 
            hypercorticisme = 'Non', 
            insuffisance_hypophysaire = 'Non', 
            hypogonadisme = 'Non', 
            diabete_type = 'Non', 
            anorexie_mentale = 'Non', 

            rhumatisme_inflammatoire = 'Non', 
            polyarthrite_rheumatoide = 'Non', 
            spondylarthrite = 'Non', 
            rhumatisme_psoriasique = 'Non', 
            lupus = 'Non', 
            autres_connectivites = 'Non', 
            pseudo_polyarthrite_rhizomelique = 'Non', 
            arterite_cellules_geantes = 'Non', 

            maladie_genetique = 'Non', 
            hemochromatose = 'Non', 
            mastocytose = 'Non', 

            pathologie_intestinale = 'Non', 
            maladie_crohn = 'Non', 
            maladie_coeliaque = 'Non', 
            bypass = 'Non', 
            hepatopathie_chronique = 'Non', 
            rectocolite_ulcero = 'Non', 

            insuffisance_renale = 'Non', 
            clairance_inferieure_30 = 'Non',

            information_complementaires = 'No observation'
        )
        self.obj.save()  

    def test_create(self):
        self.assertTrue(Diagnosis.objects.exists())

    def test_created_at(self):
        """Diagnosis must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)