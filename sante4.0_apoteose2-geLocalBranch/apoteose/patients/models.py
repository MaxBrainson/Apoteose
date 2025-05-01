from django.db import models

choices = (('Oui', 'Oui'), ('Non', 'Non'))
choices_sexe = (('Masculin', 'Masculin'), ('Féminin', 'Féminin'))
choices_hormonotherapie = (('0', 'Décapeptyl'), ('1', 'Fémara'), ('2', 'Tamoxifène'))
choices_calcium = (('Petites', 'Petites'), ('Moyennes', 'Moyennes'), ('Grandes', 'Grandes'))
choices_calcium_laquelle = (('0', 'Badoit'), ('1', 'Contrex'), ('2', 'Evian'), ('3', 'Perrier'), ('4', 'Vichy'), ('5', 'Vittel Grande Source'), ('6', 'Hépar'), ('7', 'Autre'))




class Diagnosis(models.Model):

    # Informations Générales
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    age = models.IntegerField()
    sexe = models.CharField(max_length=100, choices=choices_sexe)
    menopause = models.CharField(choices=choices, max_length=10, default="Non")
    menopause_age = models.IntegerField(null=True, blank=True)
    taille = models.IntegerField()
    taille_20 = models.IntegerField(null=True)
    poids = models.IntegerField(null=True)
    imc = models.DecimalField(decimal_places=2, max_digits=5)
    # IMCLow = models.CharField(max_length=5, choices=choices)


    # Traitements Passés
    vitamine_d = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    supplem_calcium = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    dose_calcium_journaliere = models.IntegerField(null=True)
    traitement_osteo = models.CharField(max_length=100, choices=choices, blank=True, default="Non")

    traitement_subs_menopause = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_menopause_init_date = models.DateField(null=True)
    traitement_menopause_end_date = models.DateField(null=True)

    traitement_raloxifene = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_raloxifene_init_date = models.DateField(null=True)
    traitement_raloxifene_end_date = models.DateField(null=True)

    traitement_bisphosphonates = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_risedronate = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_risedronate_init_date = models.DateField(null=True)
    traitement_risedronate_end_date = models.DateField(null=True)
    
    traitement_aledronate = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_aledronate_init_date = models.DateField(null=True)
    traitement_aledronate_end_date = models.DateField(null=True)
    
    traitement_acide_zoledronique = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_acide_zoledronique_init_date = models.DateField(null=True)
    traitement_acide_zoledronique_end_date = models.DateField(null=True)

    traitement_denosumab = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_denosumab_init_date = models.DateField(null=True)
    traitement_denosumab_end_date = models.DateField(null=True)

    traitement_teriparatide = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_teriparatide_init_date = models.DateField(null=True)
    traitement_teriparatide_end_date = models.DateField(null=True)

    bonne_observance = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    traitement_bonne_init_date = models.DateField(null=True)
    traitement_bonne_end_date = models.DateField(null=True)


    # Apport en Calcium
    quest1_jour_tasses =  models.IntegerField(default=0, null=True)
    quest1_jour_bols =  models.IntegerField(default=0, null=True)
    quest1_semaine_tasses =  models.IntegerField(default=0, null=True)
    quest1_semaine_bols =  models.IntegerField(default=0, null=True)

    quest2_semaine = models.IntegerField(default=0, null=True)

    quest3_100_semaine = models.IntegerField(default=0, null=True)
    quest3_500_semaine = models.IntegerField(default=0, null=True)
    quest3_1000_semaine = models.IntegerField(default=0, null=True)

    quest4_petit_semaine = models.IntegerField(default=0, null=True)
    quest4_grands_semaine = models.IntegerField(default=0, null=True)

    quest5_fromage_fois_semaine =models.IntegerField(default=0, null=True)
    quest5_fromage_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest6_fromage_fois_semaine = models.IntegerField(default=0, null=True)
    quest6_fromage_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest7_fois_jour = models.IntegerField(default=0, null=True)
    quest7_portions_jour = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")
    quest7_fois_semaine = models.IntegerField(default=0, null=True)
    quest7_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest8_semaine = models.IntegerField(default=0, null=True)

    quest9_semaine = models.IntegerField(default=0, null=True)
    quest9_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest10_semaine = models.IntegerField(default=0, null=True)
    quest10_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest11_semaine = models.IntegerField(default=0, null=True)
    quest11_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest12_semaine = models.IntegerField(default=0, null=True)
    quest12_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest13_semaine = models.IntegerField(default=0, null=True)
    quest13_portions_semaine = models.CharField(max_length=100, choices=choices_calcium, blank=True, default="")

    quest14_ficelles_jour = models.IntegerField(default=0, null=True)
    quest14_baguettes_jour = models.IntegerField(default=0, null=True)
    quest14_biscottes_jour = models.IntegerField(default=0, null=True)

    quest15_semaine = models.IntegerField(default=0, null=True)

    quest16_barres_semaine = models.IntegerField(default=0, null=True)
    quest16_tablettes_semaine = models.IntegerField(default=0, null=True)

    quest17_barres_semaine = models.IntegerField(default=0, null=True)
    quest17_tablettes_semaine = models.IntegerField(default=0, null=True)

    quest18_verres_jour = models.IntegerField(default=0, null=True)
    quest18_litres_jour = models.IntegerField(default=0, null=True)

    quest19_verres_jour = models.IntegerField(default=0, null=True)
    quest19_litres_jour = models.IntegerField(default=0, null=True)
    quest19_laquelle = models.CharField(max_length=100, choices=choices_calcium_laquelle, blank=True, default="")
    

    quest20_chaque_jour = models.IntegerField(default=0, null=True)

    apport_calcium = models.IntegerField(null=True)
    calcium_intake = models.IntegerField(null=True)


    # DXA Exam
    z_score_col_femur = models.FloatField(null=True)
    z_score_hache = models.FloatField(null=True)
    z_score_rachis = models.FloatField(null=True)
    z_score_extremite_distale = models.CharField(max_length=100, choices=choices)

    t_score_col_femur = models.FloatField(null=True)
    t_score_hache = models.FloatField(null=True)
    t_score_rachis = models.FloatField(null=True)
    t_score_extremite_distale = models.CharField(max_length=100, choices=choices, default="Non")

    frax = models.IntegerField(null=True)

    ## Pop-up
    z_score_femur_popup = models.CharField(max_length=100, blank=True, default="Non")
    z_score_hanche_popup = models.CharField(max_length=100, blank=True, default="Non")
    z_score_rachis_popup = models.CharField(max_length=100, blank=True, default="Non")
    z_score_extremite_popup = models.CharField(max_length=100, blank=True, default="Non")


    # Habitude
    tabagisme = models.CharField(max_length=100, choices=choices)
    alcool = models.CharField(max_length=100, choices=choices)
    activite_phsique = models.CharField(max_length=100, choices=choices)
    chutes_frequentes = models.CharField(max_length=100, choices=choices)
    traitement_vih = models.CharField(max_length=100, choices=choices)
    corticotherapie = models.CharField(max_length=100, choices=choices)
    corticotherapie_plus_3 = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    corticotherapie_plus_7_5 = models.CharField(max_length=100, choices=choices, blank=True, default="Non")
    hormonotherapie = models.CharField(max_length=100, choices=choices)
    hormonotherapie_choices = models.CharField(max_length=100, choices=choices_hormonotherapie, blank=True)


    # Neóplasie
    radiotherapie = models.CharField(max_length=100, choices=choices)
    cancer_prostate = models.CharField(max_length=100, choices=choices)
    cancer_sein = models.CharField(max_length=100, choices=choices, default="Non")

    ## Pop-up Cancer Prostate
    comorbites_associees = models.CharField(max_length=100, choices=choices, default="Non")
    castraction_chirurgiale = models.CharField(max_length=100, choices=choices, default="Non")
    frax_cancer = models.IntegerField(null=True)

    ## Pop-up Cancer Sein
    analogue_lh_rh = models.CharField(max_length=100, choices=choices, default="Non")
    tamoxifene = models.CharField(max_length=100, choices=choices, default="Non")
    horm_anastrazole = models.CharField(max_length=100, choices=choices, default="Non")
    horm_letrozole = models.CharField(max_length=100, choices=choices, default="Non")
    horm_exemestane = models.CharField(max_length=100, choices=choices, default="Non")
    amenorrhee_induite = models.CharField(max_length=100, choices=choices, default="Non")

    # Fracture
    antecedent_fracture_faible_energie = models.CharField(max_length=100, choices=choices)
    fracture_severe = models.CharField(max_length=100, choices=choices, default="Non")
    fracture_deux_vertebres = models.CharField(max_length=100, choices=choices, default="Non")
    fracture_non_severe = models.CharField(max_length=100, choices=choices, default="Non")
    fracture_fragilite_femoral = models.CharField(max_length=100, choices=choices, default="Non")


    # Antécédents
    ## Endocrinopathie
    edocrinopathie = models.CharField(max_length=100, choices=choices)
    hyperparathyroide = models.CharField(max_length=100, choices=choices, default="Non")
    hyperthyroide = models.CharField(max_length=100, choices=choices, default="Non")
    hypercorticisme = models.CharField(max_length=100, choices=choices, default="Non")
    insuffisance_hypophysaire = models.CharField(max_length=100, choices=choices, default="Non")
    hypogonadisme = models.CharField(max_length=100, choices=choices, default="Non")
    diabete_type = models.CharField(max_length=100, choices=choices, default="Non")
    anorexie_mentale = models.CharField(max_length=100, choices=choices, default="Non")

    ## Rhumatisme Inflammatoire
    rhumatisme_inflammatoire = models.CharField(max_length=100, choices=choices)
    polyarthrite_rheumatoide = models.CharField(max_length=100, choices=choices, default="Non")
    spondylarthrite = models.CharField(max_length=100, choices=choices, default="Non")
    rhumatisme_psoriasique = models.CharField(max_length=100, choices=choices, default="Non")
    lupus = models.CharField(max_length=100, choices=choices, default="Non")
    autres_connectivites = models.CharField(max_length=100, choices=choices, default="Non")
    pseudo_polyarthrite_rhizomelique = models.CharField(max_length=100, choices=choices, default="Non")
    arterite_cellules_geantes = models.CharField(max_length=100, choices=choices, default="Non")

    ## Maladie Génétique
    maladie_genetique = models.CharField(max_length=100, choices=choices)
    hemochromatose = models.CharField(max_length=100, choices=choices, default="Non")
    mastocytose = models.CharField(max_length=100, choices=choices, default="Non")
    drepanocytose = models.CharField(max_length=100, choices=choices, default="Non")

    ## Pathologie Intestinale/digestive
    pathologie_intestinale = models.CharField(max_length=100, choices=choices)
    maladie_crohn = models.CharField(max_length=100, choices=choices, default="Non")
    maladie_coeliaque = models.CharField(max_length=100, choices=choices, default="Non")
    bypass = models.CharField(max_length=100, choices=choices, default="Non")
    hepatopathie_chronique = models.CharField(max_length=100, choices=choices, default="Non")
    rectocolite_ulcero = models.CharField(max_length=100, choices=choices, default="Non")

    ## Insuffisance renale chronique
    insuffisance_renale = models.CharField(max_length=100, choices=choices)
    clairance_inferieure_30 = models.CharField(max_length=100, choices=choices, default="Non")

    # Informations Complémentaires
    information_complementaires = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    