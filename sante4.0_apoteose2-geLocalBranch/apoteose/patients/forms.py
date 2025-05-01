from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'
    

class DiagnosisForm(forms.Form):
    choices = (('Oui', 'Oui'), ('Non', 'Non'))
    choices_sexe = (('Masculin', 'Masculin'), ('Féminin', 'Féminin'))
    choices_hormonotherapie = (('0', 'Décapeptyl'), ('1', 'Fémara'), ('2', 'Tamoxifène'))
    choices_calcium = (('Petites', 'Petites'), ('Moyennes', 'Moyennes'), ('Grandes', 'Grandes'))
    choices_calcium_laquelle = (('0', 'Badoit'), ('1', 'Contrex'), ('2', 'Evian'), ('3', 'Perrier'), ('4', 'Vichy'), ('5', 'Vittel Grande Source'), ('6', 'Hépar'), ('7', 'Autre'))


    # Informations Générales
    prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input capital-letter', 'autofocus': True, 'onkeypress': "capitalizeFirstLetter(document.getElementsByClassName('capital-letter')[0]);"}))
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input capital-letter', 'onkeypress': "capitalizeFirstLetter(document.getElementsByClassName('capital-letter')[1]);"}))
    date_naissance = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input', 'onBlur': 'calculateAge()'}))
    age = forms.IntegerField(label="Âge", widget=forms.NumberInput(attrs={'class': 'form-input hidden'}), required=True)
    sexe = forms.ChoiceField(choices=choices_sexe, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onchange': 'apportCalcium();', 'onclick': 'unhideOptions("id_sexe_1", ...["menopause-hidden"]);'}))
    menopause = forms.ChoiceField(choices=choices, widget=forms.
    RadioSelect(attrs={'class': 'radio-options-label under', 'onclick': 'unhideOptions("id_menopause_0", ...["menopause-age-hidden"]);'}), required=False)
    menopause_age = forms.IntegerField(label="À Quel Âge", widget=forms.NumberInput(attrs={'class': 'form-input under'}), required=False) 
    taille = forms.IntegerField(label="Taille (cm)", widget=forms.NumberInput(attrs={'class': 'form-input'}), required=True)
    taille_20 = forms.IntegerField(label="Taille Rapportée à l'age de 20 ans (cm)", widget=forms.NumberInput(attrs={'class': 'form-input'}), required=False)
    poids = forms.IntegerField(label="Poids (kg)", widget=forms.NumberInput(attrs={'class': 'form-input', 'onBlur': 'calculateIMC();'}), required=True)
    imc = forms.DecimalField(label="IMC", widget=forms.NumberInput(attrs={'class': 'form-input hidden'}), required=True)


    # Traitements Passés
    vitamine_d = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    supplem_calcium = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_supplem_calcium_0", ...["dose-journaliere-hidden"]);'}), required=False)
    dose_calcium_journaliere = forms.IntegerField(label="Dose Journaliere", widget=forms.NumberInput(attrs={'class': 'form-input'}), required=False)
    traitement_osteo = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_osteo_0", ...["traitement-menopause-hidden", "traitement-raloxifene-hidden", "traitement-bisphosphonates-hidden", "traitement-denosumab-hidden", "traitement-teriparatide-hidden", "traitement-bonne-obs-hidden"]);'}), required=False)

    traitement_subs_menopause = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_subs_menopause_0", ... ["traitement-menopause-init-date-hidden", "traitement-menopause-end-date-hidden"]);'}), required=False)
    traitement_menopause_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_menopause_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    
    traitement_raloxifene = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_raloxifene_0", ... ["traitement-raloxifene-init-date-hidden", "traitement-raloxifene-end-date-hidden"]);'}), required=False)
    traitement_raloxifene_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_raloxifene_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    
    traitement_bisphosphonates = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_bisphosphonates_0", ... ["traitement-risedronate-hidden", "traitement-aledronate-hidden", "traitement-acide-zoledronique-hidden"]);'}), required=False)
    traitement_risedronate = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_bisphosphonates_0", ... ["traitement-risedronate-init-date-hidden", "traitement-risedronate-end-date-hidden"]);'}), required=False)
    traitement_risedronate_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_risedronate_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    
    traitement_aledronate = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_bisphosphonates_0", ... ["traitement-risedronate-init-date-hidden", "traitement-risedronate-end-date-hidden"]);'}), required=False)
    traitement_aledronate_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_aledronate_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    
    traitement_acide_zoledronique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_bisphosphonates_0", ... ["traitement-risedronate-init-date-hidden", "traitement-risedronate-end-date-hidden"]);'}), required=False)
    traitement_acide_zoledronique_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_acide_zoledronique_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)

    traitement_denosumab = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_denosumab_0", ... ["traitement-denosumab-init-date-hidden", "traitement-denosumab-end-date-hidden"]);'}), required=False)
    traitement_denosumab_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_denosumab_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
   
    traitement_teriparatide = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_traitement_teriparatide_0", ... ["traitement-teriparatide-init-date-hidden", "traitement-teriparatide-end-date-hidden"]);'}), required=False)
    traitement_teriparatide_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_teriparatide_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    
    bonne_observance = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_bonne_observance_0", ... ["traitement-bonne-init-date-hidden", "traitement-bonne-end-date-hidden"]);'}), required=False)
    traitement_bonne_init_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)
    traitement_bonne_end_date = forms.DateField(widget=DateInput(format='d-m-Y', attrs={'class': 'form-input-date'}), required=False)


    ## Pop-up Calcium
    quest1_jour_tasses = forms.IntegerField(label="Nombre de verres/tasses:", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest1_jour_bols = forms.IntegerField(label="Nombre de bols:", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest1_semaine_tasses = forms.IntegerField(label="Nombre de verres/tasses:", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest1_semaine_bols = forms.IntegerField(label="Nombre de bols:", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    
    quest2_semaine = forms.IntegerField(label="Si oui, combien par semaine?", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest3_100_semaine = forms.IntegerField(label="- Combien de pots de 100 g par semaine?", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest3_500_semaine = forms.IntegerField(label="- Combien de pots de 500 g par semaine ?", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest3_1000_semaine = forms.IntegerField(label="- Combien de pots de 1 kg par semaine ?", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest4_petit_semaine = forms.IntegerField(label="- Combien de petits modèles par semaine ?", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest4_grands_semaine = forms.IntegerField(label="- Combien de grands modèles par semaine ?", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest5_fromage_fois_semaine = forms.IntegerField(label="Si oui : Combien de fois par semaine ?", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest5_fromage_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest6_fromage_fois_semaine = forms.IntegerField(label="Si oui : Combien de fois en mangez-vous par semaine ? ", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest6_fromage_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest7_fois_jour = forms.IntegerField(label="Si oui : Combien de fois en mangez-vous par semaine ? ", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest7_portions_jour = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    quest7_fois_semaine = forms.IntegerField(label="Si oui : Combien de fois en mangez-vous par semaine ? ", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest7_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest8_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest9_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest9_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest10_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest10_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest11_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest11_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest12_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest12_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest13_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest13_portions_semaine = forms.ChoiceField(choices=choices_calcium, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest14_ficelles_jour = forms.IntegerField(label="- ficelles par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest14_baguettes_jour = forms.IntegerField(label="- baguettes par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest14_biscottes_jour = forms.IntegerField(label="- biscottes par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest15_semaine = forms.IntegerField(widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest16_barres_semaine = forms.IntegerField(label="- nombre de barres par semaine :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest16_tablettes_semaine = forms.IntegerField(label="- nombre de tablettes par semaine :", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest17_barres_semaine = forms.IntegerField(label="- nombre de barres par semaine :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest17_tablettes_semaine = forms.IntegerField(label="- nombre de tablettes par semaine :", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest18_verres_jour = forms.IntegerField(label="- nombre de verres par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest18_litres_jour = forms.IntegerField(label="- nombre de litres par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    quest19_verres_jour = forms.IntegerField(label="- nombre de verres par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest19_litres_jour = forms.IntegerField(label="- nombre de litres par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)
    quest19_laquelle = forms.ChoiceField(choices=choices_calcium_laquelle, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    quest20_chaque_jour = forms.IntegerField(label="Si oui, nombre de verres par jour :", widget=forms.NumberInput({'class': 'form-input'}), required=False)

    # Apport en Calcium
    apport_calcium = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input hidden'}), required=False)
    calcium_intake = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-input hidden'}), required=False)

    # DXA Exam
    z_score_col_femur = forms.FloatField(label="Z Score Col Fémur", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    z_score_hache = forms.FloatField(label="Z Score Hanche Totale", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    z_score_rachis = forms.FloatField(label="Z Score Rachis Lombaire", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    z_score_extremite_distale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'step': '0.01', 'onclick': 'showPopUps("id_z_score_extremite_distale_0", ...["popup-z-score"]);'}))

    t_score_col_femur = forms.FloatField(label="T Score Col Fémur", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    t_score_hache = forms.FloatField(label="T Score Hanche Totale", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    t_score_rachis = forms.FloatField(label="T Score Rachis Lombaire", widget=forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}), max_value=2, min_value=-5)
    t_score_extremite_distale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'step': '0.01', 'onclick': 'showPopUps("id_t_score_extremite_distale_0", ...["popup-t-score"]);'}))

    frax = forms.IntegerField(label="FRAX (%)", widget=forms.NumberInput(attrs={'class': 'form-input'}), required=False)

    ## Pop-up
    z_score_femur_popup = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'radio-options-label checkbox'}), required=False)
    z_score_hanche_popup = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'radio-options-label'}), required=False)
    z_score_rachis_popup = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'radio-options-label'}), required=False)
    z_score_extremite_popup = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'radio-options-label'}), required=False)


    # Habitude
    tabagisme = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    alcool = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    activite_phsique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    chutes_frequentes = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    traitement_vih = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    corticotherapie = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_corticotherapie_0", ...["corticotherapie-plus-3-mois-hidden", "corticotherapie-plus-7-5-hidden"]);'}))
    corticotherapie_plus_3 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    corticotherapie_plus_7_5 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    hormonotherapie = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_hormonotherapie_0", ...["hormonotherapie-choices-hidden"]);'}))
    hormonotherapie_choices = forms.ChoiceField(choices=choices_hormonotherapie, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)


    # Neóplasie
    radiotherapie = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}))
    cancer_prostate = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'showPopUps("id_cancer_prostate_0", ...["popup-cancer-prostate"]);'}))
    cancer_sein = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'showPopUps("id_cancer_sein_0", ...["popup-cancer-sein"]);'}))

    ## Pop-up Cancer Prostate
    comorbites_associees = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    castraction_chirurgiale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    frax_cancer = forms.IntegerField(label="FRAX Fracture de Hanche (%)", widget=forms.NumberInput(attrs={'class': 'form-input'}), required=False)

    # Pop-up Cancer Sein
    analogue_lh_rh = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    tamoxifene = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    horm_anastrazole = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    horm_letrozole = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    horm_exemestane = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    amenorrhee_induite = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    # Fracture
    antecedent_fracture_faible_energie = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_antecedent_fracture_faible_energie_0", ...["fracture-severe-hidden", "fracture-non-severe-hidden", "fracture-fragilite-femoral-hidden"]);'}))
    fracture_severe = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_fracture_severe_0", "fracture-deux-vertebres-hidden");'}), required=False)
    fracture_deux_vertebres = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    fracture_non_severe = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    fracture_fragilite_femoral = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)


    # Antécédents
    ## Endocrinopathie
    edocrinopathie = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_edocrinopathie_0", ...["hyperparathyroide-hidden", "hyperthyroide-hidden", "hypercorticisme-hidden", "insuffisance-hypophysaire-hidden", "hypogonadisme-hidden", "diabete-type-hidden", "anorexie-mentale-hidden"]);'}))
    hyperparathyroide = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    hyperthyroide = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    hypercorticisme = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    insuffisance_hypophysaire = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    hypogonadisme = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    diabete_type = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    anorexie_mentale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    ## Rhumatisme Inflammatoire
    rhumatisme_inflammatoire = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_rhumatisme_inflammatoire_0", ...["polyarthrite-rheumatoide-hidden", "spondylarthrite-hidden", "rhumatisme-psoriasique-hidden", "lupus-hidden", "autres-connectivites-hidden", "pseudo-polyarthrite-rhizomélique-hidden", "arterite-cellules-geantes-hidden"]);'}))
    polyarthrite_rheumatoide = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    spondylarthrite = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    rhumatisme_psoriasique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    lupus = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    autres_connectivites = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    pseudo_polyarthrite_rhizomelique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    arterite_cellules_geantes = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    ## Maladie Génétique
    maladie_genetique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_maladie_genetique_0", ...["hemochromatose-hidden", "mastocytose-hidden", "drepanocytose-hidden"]);'}))
    hemochromatose = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    mastocytose = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    drepanocytose = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    ## Pathologie Intestinale/digestive
    pathologie_intestinale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_pathologie_intestinale_0", ...["maladie-crohn-hidden", "maladie-coeliaque-hidden", "bypass-hidden", "hepatopathie-chronique-hidden", "rectocolite-ulcero-hidden"]);'}))
    maladie_crohn = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    maladie_coeliaque = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    bypass = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    hepatopathie_chronique = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)
    rectocolite_ulcero = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    ## Insuffisance renale chronique
    insuffisance_renale = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label', 'onclick': 'unhideOptions("id_insuffisance_renale_0", ...["clairance-inferieure-30-hidden"]);'}))
    clairance_inferieure_30 = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs={'class': 'radio-options-label'}), required=False)

    # Informations Complémentaires
    information_complementaires = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Ecrivez plus d'informations sur le patient", 'rows': 5}), required=False)

