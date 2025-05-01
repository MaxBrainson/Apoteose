/* LOGIN PAGE */
function changeActive(name) {
    const classe = document.getElementById(name);

    if (classe.classList.contains('active')) {
        classe.classList.remove('active');
    } else {
        classe.classList.add('active');
    }
}

// FORMS PAGE

function capitalizeFirstLetter(element) {
    element.value = element.value.charAt(0).toUpperCase() + element.value.slice(1);
}

function unhideOptions(baseElementId, ...changeElementId) {
    for (let id of changeElementId) {
        if (document.getElementById(baseElementId).checked) {
            document.getElementById(id).style.display = 'flex';
        } else {
            document.getElementById(id).style.display = 'none';
        }
    }
}

function showPopUps(baseElementId, ...changeElementId) {
    for (let id of changeElementId) {
        if (document.getElementById(baseElementId).checked) {
            document.getElementById(id).style.visibility = 'visible';
        } else {
            document.getElementById(id).style.visibility = 'hidden';
        }
    }
}


function cancelPopUps(baseElementId, popUpId, ...unselectIds) {
    for (let id of unselectIds) {
        if (document.getElementById(id).type === "checkbox" || document.getElementById(id).type === "radio") {
            document.getElementById(id).checked = false;
        } else if (document.getElementById(id).type === "number" || document.getElementById(id).type === "textarea") {
            document.getElementById(id).value = "";
        }
    }
    if (document.getElementById(baseElementId).type === "radio") {
        document.getElementById(baseElementId.replace("0", "1")).checked = true;
        document.getElementById(popUpId).style.visibility = 'hidden';
    } else if (document.getElementById(baseElementId).type === "button") {
        document.getElementById(popUpId).style.visibility = 'hidden';
    }
}


function savePopUp(popUpId) {
    document.getElementById(popUpId).style.visibility = 'hidden';
}


function clearForm(form) {
    document.getElementById(form).reset();
}


function redirect() {
    setTimeout(myURL, 4000);
}


function myURL() {
    document.location.href = '/login/';
}


function claireForm() {
    document.getElementById('diagnosisForm').reset();
    document.location.href = '/home/';
}


function calculateAge() {
    var dobField = document.getElementById("id_date_naissance");
    var ageField = document.getElementById("id_age");
    
    if (dobField.value) {
        var dob = new Date(dobField.value);
        var today = new Date();
        var age = today.getFullYear() - dob.getFullYear();
        
        // Ajuster l'âge si l'anniversaire n'est pas encore passé cette année
        if (today.getMonth() < dob.getMonth() || (today.getMonth() === dob.getMonth() && today.getDate() < dob.getDate())) {
            age--;
        }
        
        ageField.value = age;
        // Appeler la fonction pour mettre à jour les scores en fonction de l'âge
        toggleScoresByAge(age);
    }
}

function toggleScoresByAge(age) {
    if (age <= 24) {
        // Afficher les Z-scores et masquer les T-scores
        document.querySelectorAll('.z-score-row').forEach(function(row) {
            row.style.display = 'flex';
        });
        document.querySelectorAll('.t-score-row').forEach(function(row) {
            row.style.display = 'none';
        });
    } else {
        // Afficher les T-scores et masquer les Z-scores
        document.querySelectorAll('.z-score-row').forEach(function(row) {
            row.style.display = 'none';
        });
        document.querySelectorAll('.t-score-row').forEach(function(row) {
            row.style.display = 'flex';
        });
    }
}

// Initialiser l'affichage des scores au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    var ageField = document.getElementById("id_age");
    if (ageField && ageField.value) {
        toggleScoresByAge(parseInt(ageField.value));
    }
});


function calculateIMC() {
    poids = document.getElementById('id_poids').value;
    taille = document.getElementById('id_taille').value;

    imc = (poids / ((taille / 100) * (taille / 100))).toFixed(2);

    imc_html = document.getElementById('calculated-imc');

    imc_html.value = imc;
    imc_html.innerHTML = imc;
    document.getElementById('id_imc').value = imc;
}


// function apportCalcium() {
//     age = document.getElementById('id_age').value;
//     if (document.getElementById('id_sexe_0').checked) {
//         gender = 0; // Masculin
//     } else if (document.getElementById('id_sexe_1').checked) {
//         gender = 1; // Feminin
//     }

//     if (age >= 1 && age <= 3) {
//         calciumIntake = 500;
//     } else if (age >= 4 && age <= 6) {
//         calciumIntake = 700;
//     } else if (age >= 7 && age <= 9) {
//         calciumIntake = 900;
//     } else if (age >= 10 && age <= 18) {
//         calciumIntake = 1200;
//     } else if (age >= 55 && gender === 1) {
//         calciumIntake = 1200;
//     } else if (age >= 65 && gender === 0) {
//         calciumIntake = 1200;
//     } else if (age >= 19) {
//         calciumIntake = 900;
//     }

//     calcium_html = document.getElementById('calculated-calcium-apport');
//     calcium_html.value = calciumIntake;
//     calcium_html.innerHTML = calciumIntake + ' mg/jour';
//     document.getElementById('id_apport_calcium').value = calciumIntake;

// }


function checkFRAX() {
    age = document.getElementById('id_age').value;
    if (age <= 24) {
        // Afficher les Z-scores et masquer les T-scores
        document.querySelectorAll('.z-score-row').forEach(function(row) {
            row.style.display = 'block';
        });
        document.querySelectorAll('.t-score-row').forEach(function(row) {
            row.style.display = 'none';
        });
    } else {
        // Afficher les T-scores et masquer les Z-scores
        document.querySelectorAll('.z-score-row').forEach(function(row) {
            row.style.display = 'none';
        });
        document.querySelectorAll('.t-score-row').forEach(function(row) {
            row.style.display = 'block';
        });
    }
}

var nonRadioOptions = Array.from(document.querySelectorAll('input[type="radio"][value="Non"]')).filter(function (radioOption) {
    return !radioOption.closest('.modal');
});

nonRadioOptions.forEach(function (radioOption) {
    radioOption.checked = true;
});

var closeModalButton = document.getElementById("btn-claire-calcium");
var modalCalcium = document.getElementById("modalCalcium");

closeModalButton.addEventListener('click', function () {
    // Clear input values
    var inputs = modalCalcium.querySelectorAll('input');
    inputs.forEach(function (input) {
        input.value = '';
    });

});


class Calcium {
    constructor(patient) {
        this.Patient = patient;
        this.Dictionary_Value_Food_Original = {
            JouLaiVer: [100, 0, 0],
            JouLaiBol: [300, 0, 0],
            SemLaiVer: [14, 0, 0],
            SemLaiBol: [43, 0, 0],
            Yaourts: [21, 0, 0],
            Pots100gr: [14, 0, 0],
            Pots500gr: [68, 0, 0],
            Pots1kg: [136, 0, 0],
            PetModeles: [4, 0, 0],
            GraModeles: [8, 0, 0],
            PetFromDur: [19, 0, 0],
            MoyFromDur: [38, 0, 0],
            GraFromDur: [56, 0, 0],
            PetFromMol: [9, 0, 0],
            MoyFromMol: [17, 0, 0],
            GraFromMol: [26, 0, 0],
            JouPetVian: [8, 0, 0],
            JouMoyVian: [15, 0, 0],
            JouGraVian: [23, 0, 0],
            SemPetVian: [1, 0, 0],
            SemMoyVian: [2, 0, 0],
            SemGraVian: [3, 0, 0],
            oeufs: [4, 0, 0],
            PetPomDeTer: [1, 0, 0],
            MoyPomDeTer: [3, 0, 0],
            GraPomDeTer: [4, 0, 0],
            PetFrites: [7, 0, 0],
            MoyFrites: [14, 0, 0],
            GraFrites: [21, 0, 0],
            PetSemoule: [1, 0, 0],
            MoySemoule: [1, 0, 0],
            GraSemoule: [2, 0, 0],
            PetLegSecs: [4, 0, 0],
            MoyLegSecs: [8, 0, 0],
            GraLegSecs: [11, 0, 0],
            PetLegVert: [7, 0, 0],
            MoyLegVert: [13, 0, 0],
            GraLegVert: [30, 0, 0],
            Ficelles: [25, 0, 0],
            Baguettes: [50, 0, 0],
            Biscottes: [4, 0, 0],
            Fruits: [4, 0, 0],
            BarChocLait: [6, 0, 0],
            TabChocLait: [31, 0, 0],
            BarChocNoir: [2, 0, 0],
            TabChocNoir: [9, 0, 0],
            VerEauRubinet: [9, 0, 0],
            LitEauRubinet: [90, 0, 0],
            VerEauMinBad: [22, 0, 0],
            VerEauMinCon: [46, 0, 0],
            VerEauMinEvi: [8, 0, 0],
            VerEauMinPer: [14, 0, 0],
            VerEauMinVic: [8, 0, 0],
            VerEauMinVit: [20, 0, 0],
            VerEauMinHep: [55, 0, 0],
            VerEauMinAut: [10, 0, 0],
            LitEauMinBad: [220, 0, 0],
            LitEauMinCon: [460, 0, 0],
            LitEauMinEvi: [80, 0, 0],
            LitEauMinPer: [140, 0, 0],
            LitEauMinVic: [80, 0, 0],
            LitEauMinVit: [200, 0, 0],
            LitEauMinHep: [550, 0, 0],
            LitEauMinAut: [100, 0, 0],
            VerVin: [7, 0, 0]
        };
        this.TotalCalcium = 0;
        this.CalciumIntake = 0;
        this.CalciumVar = '';
    }

    CalculateCalciumIntake() {
        this.TotalCalcium = 0;

        this.Dictionary_Value_Food_Original["JouLaiVer"][1] = this.Patient.quest1_jour_tasses;
        this.Dictionary_Value_Food_Original["JouLaiBol"][1] = this.Patient.quest1_jour_bols;
        this.Dictionary_Value_Food_Original["SemLaiVer"][1] = this.Patient.quest1_semaine_tasses;
        this.Dictionary_Value_Food_Original["SemLaiBol"][1] = this.Patient.quest1_semaine_bols;

        this.Dictionary_Value_Food_Original["Yaourts"][1] = this.Patient.quest2_semaine;
        
        this.Dictionary_Value_Food_Original["Pots100gr"][1] = this.Patient.quest3_100_semaine;
        this.Dictionary_Value_Food_Original["Pots500gr"][1] = this.Patient.quest3_500_semaine;
        this.Dictionary_Value_Food_Original["Pots1kg"][1] = this.Patient.quest3_1000_semaine;
        
        this.Dictionary_Value_Food_Original["PetModeles"][1] = this.Patient.quest4_petit_semaine;
        this.Dictionary_Value_Food_Original["GraModeles"][1] = this.Patient.quest4_grands_semaine;
        
        if (this.Patient.quest5_fromage_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetFromDur"][1] = this.Patient.quest5_fromage_fois_semaine;
        }
        if (this.Patient.quest5_fromage_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyFromDur"][1] = this.Patient.quest5_fromage_fois_semaine;
        }
        if (this.Patient.quest5_fromage_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraFromDur"][1] = this.Patient.quest5_fromage_fois_semaine;
        }
        
        if (this.Patient.quest6_fromage_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetFromMol"][1] = this.Patient.quest6_fromage_fois_semaine;
        }
        if (this.Patient.quest6_fromage_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyFromMol"][1] = this.Patient.quest6_fromage_fois_semaine;
        }
        if (this.Patient.quest6_fromage_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraFromMol"][1] = this.Patient.quest6_fromage_fois_semaine;
        }
        
        if (this.Patient.quest7_portions_jour === "Petites") {
            this.Dictionary_Value_Food_Original["JouPetVian"][1] = this.Patient.quest7_fois_jour;
        }
        if (this.Patient.quest7_portions_jour === "Moyennes") {
            this.Dictionary_Value_Food_Original["JouMoyBian"][1] = this.Patient.quest7_fois_jour;
        }
        if (this.Patient.quest7_portions_jour === "Grandes") {
            this.Dictionary_Value_Food_Original["JouGraVian"][1] = this.Patient.quest7_fois_jour;
        }

        if (this.Patient.quest7_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["SemPetVian"][1] = this.Patient.quest7_fois_semaine;
        }
        if (this.Patient.quest7_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["SemMoyBian"][1] = this.Patient.quest7_fois_semaine;
        }
        if (this.Patient.quest7_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["SemGraVian"][1] = this.Patient.quest7_fois_semaine;
        }
        
        this.Dictionary_Value_Food_Original["oeufs"][1] = this.Patient.quest8_semaine;
        
        if (this.Patient.quest9_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetPomDeTer"][1] = this.Patient.quest9_semaine;
        }
        if (this.Patient.quest9_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyPomDeTer"][1] = this.Patient.quest9_semaine;
        }
        if (this.Patient.quest9_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraPomDeTer"][1] = this.Patient.quest9_semaine;
        }
        
        if (this.Patient.quest10_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetFrites"][1] = this.Patient.quest10_semaine;
        }
        if (this.Patient.quest10_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyFrites"][1] = this.Patient.quest10_semaine;
        }
        if (this.Patient.quest10_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraFrites"][1] = this.Patient.quest10_semaine;
        }
        
        if (this.Patient.quest11_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetSemoule"][1] = this.Patient.quest11_semaine;
        }
        if (this.Patient.quest11_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoySemoule"][1] = this.Patient.quest11_semaine;
        }
        if (this.Patient.quest11_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraSemoule"][1] = this.Patient.quest11_semaine;
        }

        if (this.Patient.quest12_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetLegSecs"][1] = this.Patient.quest12_semaine;
        }
        if (this.Patient.quest12_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyLegSecs"][1] = this.Patient.quest12_semaine;
        }
        if (this.Patient.quest12_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraLegSecs"][1] = this.Patient.quest12_semaine;
        }
        
        if (this.Patient.quest13_portions_semaine === "Petites") {
            this.Dictionary_Value_Food_Original["PetLegVert"][1] = this.Patient.quest13_semaine;
        }
        if (this.Patient.quest13_portions_semaine === "Moyennes") {
            this.Dictionary_Value_Food_Original["MoyLegVert"][1] = this.Patient.quest13_semaine;
        }
        if (this.Patient.quest13_portions_semaine === "Grandes") {
            this.Dictionary_Value_Food_Original["GraLegVert"][1] = this.Patient.quest13_semaine;
        }
        
        this.Dictionary_Value_Food_Original["Ficelles"][1] = this.Patient.quest14_ficelles_jour;
        this.Dictionary_Value_Food_Original["Baguettes"][1] = this.Patient.quest14_baguettes_jour;
        this.Dictionary_Value_Food_Original["Biscottes"][1] = this.Patient.quest14_biscottes_jour;
        
        this.Dictionary_Value_Food_Original["Fruits"][1] = this.Patient.quest15_semaine;
        
        this.Dictionary_Value_Food_Original["BarChocLait"][1] = this.Patient.quest16_barres_semaine;
        this.Dictionary_Value_Food_Original["TabChocLait"][1] = this.Patient.quest16_tablettes_semaine;
        
        this.Dictionary_Value_Food_Original["BarChocNoir"][1] = this.Patient.quest17_barres_semaine;
        this.Dictionary_Value_Food_Original["TabChocNoir"][1] = this.Patient.quest17_tablettes_semaine;
        
        this.Dictionary_Value_Food_Original["VerEauRubinet"][1] = this.Patient.quest18_verres_jour;
        this.Dictionary_Value_Food_Original["LitEauRubinet"][1] = this.Patient.quest18_litres_jour;

        if (this.Patient.quest19_laquelle === "0") {
            this.Dictionary_Value_Food_Original["VerEauMinBad"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "1") {
            this.Dictionary_Value_Food_Original["VerEauMinCon"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "2") {
            this.Dictionary_Value_Food_Original["VerEauMinEvi"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "3") {
            this.Dictionary_Value_Food_Original["VerEauMinPer"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "4") {
            this.Dictionary_Value_Food_Original["VerEauMinVic"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "5") {
            this.Dictionary_Value_Food_Original["VerEauMinVit"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "6") {
            this.Dictionary_Value_Food_Original["VerEauMinHep"][1] = this.Patient.quest19_verres_jour;
        }
        if (this.Patient.quest19_laquelle === "7") {
            this.Dictionary_Value_Food_Original["VerEauMinAut"][1] = this.Patient.quest19_verres_jour;
        }
        
        if (this.Patient.quest19_laquelle === "0") {
            this.Dictionary_Value_Food_Original["LitEauMinBad"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "1") {
            this.Dictionary_Value_Food_Original["LitEauMinCon"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "2") {
            this.Dictionary_Value_Food_Original["LitEauMinEvi"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "3") {
            this.Dictionary_Value_Food_Original["LitEauMinPer"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "4") {
            this.Dictionary_Value_Food_Original["LitEauMinVic"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "5") {
            this.Dictionary_Value_Food_Original["LitEauMinVit"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "6") {
            this.Dictionary_Value_Food_Original["LitEauMinHep"][1] = this.Patient.quest19_litres_jour;
        }
        if (this.Patient.quest19_laquelle === "7") {
            this.Dictionary_Value_Food_Original["LitEauMinAut"][1] = this.Patient.quest19_litres_jour;
        }
        
        
        this.Dictionary_Value_Food_Original["VerVin"][1] = this.Patient.quest20_chaque_jour;



        for (const food in this.Dictionary_Value_Food_Original) {
            if (this.Dictionary_Value_Food_Original.hasOwnProperty(food)) {
                const quantity = this.Dictionary_Value_Food_Original[food][1];
                if (quantity !== '' && quantity !== 0) {
                    this.Dictionary_Value_Food_Original[food][2] =
                        parseInt(quantity) * this.Dictionary_Value_Food_Original[food][0];
                }
            }
        }

        for (const food in this.Dictionary_Value_Food_Original) {
            if (this.Dictionary_Value_Food_Original.hasOwnProperty(food)) {
                this.TotalCalcium += this.Dictionary_Value_Food_Original[food][2];
            }
        }

        const age = this.Patient.age;
        if (age !== 0) {
            if (age >= 1 && age <= 3) {
                this.CalciumIntake = 500;
            } else if (age >= 4 && age <= 6) {
                this.CalciumIntake = 700;
            } else if (age >= 7 && age <= 9) {
                this.CalciumIntake = 900;
            } else if (age >= 10 && age <= 18) {
                this.CalciumIntake = 1200;
            } else if (age >= 19) {
                this.CalciumIntake = 900;
            }

            if (age >= 55 && this.Patient.sexe === 1) {
                this.CalciumIntake = 1200;
            } else if (age > 65 && this.Patient.sexe === 0) {
                this.CalciumIntake = 1200;
            }
        }

        //   this.Patient.apport_calcium = this.TotalCalcium;
        //   this.Patient.calcium_intake = this.CalciumIntake;

        this.CalciumVar = `${this.TotalCalcium} / ${this.CalciumIntake} mg/jour`;
    }
}



const closeCalciumModal = document.getElementById("btn-save-calcium");
const form = document.getElementById("diagnosisForm");

closeCalciumModal.addEventListener('click', () => {
    if (document.getElementById('id_sexe_0').checked) {
        sexe = 0; // Masculin
    } else if (document.getElementById('id_sexe_1').checked) {
        sexe = 1; // Feminin
    }

    const patient = {
        age: form.elements.id_age.value,
        sexe: sexe,

        quest1_jour_tasses: form.elements.quest1_jour_tasses.value,
        quest1_jour_bols: form.elements.quest1_jour_bols.value,
        quest1_semaine_tasses: form.elements.quest1_semaine_tasses.value,
        quest1_semaine_bols: form.elements.quest1_semaine_bols.value,

        quest2_semaine: form.elements.quest2_semaine.value,

        quest3_100_semaine: form.elements.quest3_100_semaine.value,
        quest3_500_semaine: form.elements.quest3_500_semaine.value,
        quest3_1000_semaine: form.elements.quest3_1000_semaine.value,

        quest4_petit_semaine: form.elements.quest4_petit_semaine.value,
        quest4_grands_semaine: form.elements.quest4_grands_semaine.value,

        quest5_fromage_fois_semaine: form.elements.quest5_fromage_fois_semaine.value,
        quest5_fromage_portions_semaine: form.elements.quest5_fromage_portions_semaine.value,

        quest6_fromage_fois_semaine: form.elements.quest6_fromage_fois_semaine.value,
        quest6_fromage_portions_semaine: form.elements.quest6_fromage_portions_semaine.value,

        quest7_fois_jour: form.elements.quest7_fois_jour.value,
        quest7_portions_jour: form.elements.quest7_portions_jour.value,
        quest7_fois_semaine: form.elements.quest7_fois_semaine.value,
        quest7_portions_semaine: form.elements.quest7_portions_semaine.value,

        quest8_semaine: form.elements.quest8_semaine.value,

        quest9_semaine: form.elements.quest9_semaine.value,
        quest9_portions_semaine: form.elements.quest9_portions_semaine.value,

        quest10_semaine: form.elements.quest10_semaine.value,
        quest10_portions_semaine: form.elements.quest10_portions_semaine.value,

        quest11_semaine: form.elements.quest11_semaine.value,
        quest11_portions_semaine: form.elements.quest11_portions_semaine.value,

        quest12_semaine: form.elements.quest12_semaine.value,
        quest12_portions_semaine: form.elements.quest12_portions_semaine.value,

        quest13_semaine: form.elements.quest13_semaine.value,
        quest13_portions_semaine: form.elements.quest13_portions_semaine.value,

        quest14_ficelles_jour: form.elements.quest14_ficelles_jour.value,
        quest14_baguettes_jour: form.elements.quest14_baguettes_jour.value,
        quest14_biscottes_jour: form.elements.quest14_biscottes_jour.value,

        quest15_semaine: form.elements.quest15_semaine.value,

        quest16_barres_semaine: form.elements.quest16_barres_semaine.value,
        quest16_tablettes_semaine: form.elements.quest16_tablettes_semaine.value,

        quest17_barres_semaine: form.elements.quest17_barres_semaine.value,
        quest17_tablettes_semaine: form.elements.quest17_tablettes_semaine.value,

        quest18_verres_jour: form.elements.quest18_verres_jour.value,
        quest18_litres_jour: form.elements.quest18_litres_jour.value,

        quest19_verres_jour: form.elements.quest19_verres_jour.value,
        quest19_litres_jour: form.elements.quest19_litres_jour.value,
        quest19_laquelle: form.elements.quest19_laquelle.value,

        quest20_chaque_jour: form.elements.quest20_chaque_jour.value,
    };

    // Create an instance of the Calcium class
    const calcium = new Calcium(patient);

    // Call the CalculateCalciumIntake method
    calcium.CalculateCalciumIntake();

    // Access the calculated values
    const apportCalcium = calcium.TotalCalcium;
    const calciumIntake = calcium.CalciumIntake;
    const calciumVar = calcium.CalciumVar;

    // Use the calculated values as needed
    console.log('Apport Calcium:', apportCalcium);
    console.log('Calcium Intake:', calciumIntake);
    console.log('Calcium Var:', calciumVar);

    calcium_html = document.getElementById('calculated-calcium-apport');
    calcium_html.value = calciumVar;
    calcium_html.innerHTML = calciumVar;
    document.getElementById('id_apport_calcium').value = apportCalcium;
    document.getElementById('id_calcium_intake').value = calciumIntake;

});

// Ajouter un écouteur d'événement sur le champ âge
document.getElementById('id_age').addEventListener('change', checkFRAX);