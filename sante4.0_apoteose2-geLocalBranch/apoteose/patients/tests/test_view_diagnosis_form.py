from datetime import datetime
from django.test import TestCase
from apoteose.patients.forms import DiagnosisForm
from apoteose.patients.models import Diagnosis
from django.core import mail


class DiagnosisFormGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/form/')

    def test_get(self):
        """GET /form/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use form/diagnosisForm.html"""
        self.assertTemplateUsed(self.response, 'form/diagnosisForm.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 185),
                ('submit', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
    
    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have diagnosis form"""
        form = self.response.context['form']
        self.assertIsInstance(form, DiagnosisForm)


class DiagnosisPostValid(TestCase):
    def setUp(self):
        data = dict(
            prenom = 'Geovana', 
            nom = 'Sousa', 
            date_naissance = '2000-07-19', 
            age = '22', 
            sexe = 'Féminin', 
            menopause = 'Non',
            menopause_age = "",
            taille = '165', 
            taille_20 = '165', 
            poids = '65', 
            imc = '23.89',

            vitamine_d = 'Non', 
            supplem_calcium = 'Non', 
            dose_calcium_journaliere = '1200', 
            traitement_osteo = 'Non', 
            traitement_subs_menopause = 'Non',  
            traitement_menopause_init_date = "",  
            traitement_menopause_end_date = "",  
            traitement_raloxifene = 'Non', 
            traitement_raloxifene_init_date = "", 
            traitement_raloxifene_end_date = "", 
            traitement_bisphosphonates = "Non",
            traitement_risedronate = "Non",
            traitement_risedronate_init_date = "",
            traitement_risedronate_end_date = "",
            traitement_aledronate = 'Non',
            traitement_aledronate_init_date = "",
            traitement_aledronate_end_date = "",
            traitement_acide_zoledronique = "Non",
            traitement_acide_zoledronique_init_date = "",
            traitement_acide_zoledronique_end_date = "",
            traitement_denosumab = 'Non', 
            traitement_denosumab_init_date = "", 
            traitement_denosumab_end_date = "", 
            traitement_teriparatide ='Non', 
            traitement_teriparatide_init_date ="", 
            traitement_teriparatide_end_date ="", 
            bonne_observance = 'Non', 
            traitement_bonne_init_date = "", 
            traitement_bonne_end_date = "", 

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
            drepanocytose = 'Non',

            pathologie_intestinale = 'Non', 
            maladie_crohn = 'Non', 
            maladie_coeliaque = 'Non', 
            bypass = 'Non', 
            hepatopathie_chronique = 'Non', 
            rectocolite_ulcero = 'Non', 

            insuffisance_renale = 'Non', 
            clairance_inferieure_30 = 'Non',

            information_complementaires = 'No observation',
        )

        self.resp = self.client.post('/form/', data)

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    # def test_save_diagnosis(self):
    #     self.assertTrue(Diagnosis.objects.exists())


class DiagnosisPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/form/', {})
        
    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'form/diagnosisForm.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, DiagnosisForm)
    
    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_diagnosis(self):
        self.assertFalse(Diagnosis.objects.exists())

