from django.test import TestCase

from apoteose.patients.forms import DiagnosisForm
from apoteose.patients.models import Diagnosis
from apoteose.patients.classes.DecisionTree import DecisionTree


class DecisionChoice(TestCase):
    def test_pediatrique_higher(self):
        data = dict(
            age = 22,
            taille = 165,
            taille_20 = 165,
            z_score_col_femur = -1.0,
            z_score_hache = 0,
            z_score_rachis = 1,
        )
        # self.resp = self.client.post('/form/', data)
        self.path = DecisionTree().DecisionChoice(data)

        self.assertEqual(self.path, [False,-1.0,'->','Pediatrique','Tscore>-2','Perte de taille de 2 cm : Pas besoin de radiographie'])
    

    def test_pediatrique_lower(self):
        data = dict(
            age = 22,
            taille = 165,
            taille_20 = 165,
            z_score_col_femur = -3.0,
            z_score_hache = 0,
            z_score_rachis = 1,
        )
        self.resp = self.client.post('/form/', data)
        self.path = DecisionTree().DecisionChoice(data)

        self.assertEqual(self.path, [True, -3.0, '->', 'Pediatrique', 'Tscore<=-2',  'Perte de taille de 2 cm : Pas besoin de radiographie'])

    
    # def test_corticotherapie_oui_masculin(self):
    #     data = dict(
    #         age = 25,
    #         sexe = 'Masculin',

    #     )