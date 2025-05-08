import os
from io import BytesIO
from django.http import FileResponse, HttpResponseRedirect, StreamingHttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import base64
from django import template
from django.shortcuts import redirect
from django.contrib.staticfiles.finders import find as find_static_file
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime

from apoteose.patients.models import Diagnosis
from apoteose.patients.forms import DiagnosisForm
from apoteose.patients.classes.Diagnose import DiagnoseAnalysis
from apoteose.patients.classes.DecisionTree import DecisionTree



def form(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)
    

def create(request):
    form = DiagnosisForm(request.POST)
    
    if not form.is_valid():
        print("Erreur de validation du formulaire:", form.errors)
        return render(request, 'form/diagnosisForm.html', {'form': form})

    form_final = form.cleaned_data
    print("Données du formulaire validées:", form_final)

    try:
        Diagnosis.objects.create(**form.cleaned_data)
        print("Diagnosis créé avec succès")
    except Exception as e:
        print("Erreur lors de la création du Diagnosis:", str(e))

    try:
        pdf_data = DiagnoseAnalysis(form_final).context
        print("Données pour le PDF générées:", pdf_data)
    except Exception as e:
        print("Erreur lors de la génération des données du PDF:", str(e))

    try:
        download = download_pdf('reportTest.html', pdf_data)
        print("PDF généré avec succès")
        return download
    except Exception as e:
        print("Erreur lors de la génération du PDF:", str(e))
        return HttpResponse("Erreur lors de la génération du PDF", status=500)


def new(request):
    return render(request, 'form/diagnosisForm.html', {'form': DiagnosisForm()})




def render_to_pdf(template_src, context_dict={}):
    try:
        template = get_template(template_src)
        print("Template chargé:", template_src)
        
        html = template.render(context_dict)
        print("HTML généré avec succès")
        
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        
        if pdf.err:
            print("Erreur lors de la génération du PDF:", pdf.err)
            return None
            
        print("PDF généré avec succès")
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    except Exception as e:
        print("Erreur dans render_to_pdf:", str(e))
        return None


#def download_pdf(template_src, context_dict={}):
 #   pdf = render_to_pdf(template_src, context_dict)
  #  response = HttpResponse(pdf, content_type='application/pdf')
   # filename = "Diagnostic%s.pdf" %("")
   # content = "attachment; filename=%s" %(filename)
    #response['Content-Disposition'] = content
    #return response


def createNewModelsFields(patientData):
    patientData['IMClow'] = "Oui" if patientData["imc"] < 18 else "Non" 
    # patientData['Calc'] = 
    # patientData['NoYesPath'] = 
    # patientData['PathAsso'] = 
    # patientData['NoInduct'] = 
    # patientData['Inducteurs'] = 
    # patientData['NoTraitSpe'] = 
    # patientData['TraiSpe'] = 
    # patientData['Cortico'] = 
    # patientData['PlusDe'] = 
    # patientData['Score'] = 
    # patientData['RachisClass'] = 
    # patientData['FemurClass'] = 
    # patientData['HancheClass'] = 
    # patientData['DistalClass'] = 
    # patientData['Diagnose'] = 
    # patientData['PathDiagnose'] = DecisionTree().DecisionChoice(patientData)
    # patientData['Traitement'] = 
    # patientData['InfoTraitement'] = 
    # patientData['Hyperpa'] = 
    # patientData['PhraseTraitement'] = 
    # patientData['AdviseTraitement'] = 
    # patientData['AdviseGeneral'] = 
    # patientData['PossivleVitD'] = 
    # patientData['DiagnoseCalcium'] = 

def get_diagnosis(request):
    """
    Affiche le diagnostic de manière dynamique
    """
    if request.method == 'POST':
        try:
            
            # Convertir les champs numériques
            patient_data = request.POST.copy()  # Crée une copie mutable
            
            # Liste des champs qui doivent être convertis en float/int
            numeric_fields = [
                'age', 'taille', 'poids', 'imc', 
                'z_score_rachis', 'z_score_col_femur', 'z_score_hache',
                't_score_rachis', 't_score_col_femur', 't_score_hache', 'taille_20'
            ]
            
            for field in numeric_fields:
                if field in patient_data and patient_data[field]:
                    try:
                        patient_data[field] = float(patient_data[field])
                    except (ValueError, TypeError):
                        patient_data[field] = None  
           
            print("Données reçues:", patient_data)
            
            # Vérification des données requises
            required_fields = ['nom', 'prenom', 'age', 'sexe']
            missing_data = [field for field in required_fields if not patient_data.get(field)]
            
            if missing_data:
                return JsonResponse({
                    'error': f'Données manquantes: {", ".join(missing_data)}'
                }, status=400)
            
            
            # Génération du diagnostic
            diagnosis = DiagnoseAnalysis(patient_data)
            diagnosis_data = diagnosis.context
            print("Données du diagnostic générées:", diagnosis_data)
            
            # Création du répertoire reports s'il n'existe pas
            reports_dir = os.path.join(settings.MEDIA_ROOT, 'reports')
            os.makedirs(reports_dir, exist_ok=True)
            
            # Génération du rapport PDF
            report_filename = f"diagnosis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            report_path = os.path.join(reports_dir, report_filename)
            
            # Préparation du contexte pour le PDF
            pdf_context = {
                'prenom': patient_data.get('prenom', ''),
                'nom': patient_data.get('nom', ''),
                'sexe': patient_data.get('sexe', ''),
                'age': patient_data.get('age', ''),
                'taille': patient_data.get('taille', ''),
                'poids': patient_data.get('poids', ''),
                'imc': patient_data.get('imc', ''),
                'date_naissance': patient_data.get('date_naissance', ''),
                'tabagisme': patient_data.get('tabagisme', ''),
                'alcool': patient_data.get('alcool', ''),
                'activite_phsique': patient_data.get('activite_phsique', ''),
                'antecedent_fracture_faible_energie': patient_data.get('antecedent_fracture_faible_energie', ''),
                'fracture_fragilite_femoral': patient_data.get('fracture_fragilite_femoral', ''),
                'chutes_frequentes': patient_data.get('chutes_frequentes', ''),
                'information_complementaires': patient_data.get('information_complementaires', ''),
                'z_score_rachis': diagnosis_data.get('z_score_rachis', ''),
                'z_score_col_femur': diagnosis_data.get('z_score_col_femur', ''),
                'z_score_hache': diagnosis_data.get('z_score_hache', ''),
                'z_score_extremite_distale': diagnosis_data.get('z_score_extremite_distale', ''),
                'RachisClass': diagnosis_data.get('RachisClass', ''),
                'FemurClass': diagnosis_data.get('FemurClass', ''),
                'HancheClass': diagnosis_data.get('HancheClass', ''),
                'DistalClass': diagnosis_data.get('DistalClass', ''),
                'Diagnose': diagnosis_data.get('Diagnose', ''),
                'PathDiagnose': diagnosis_data.get('PathDiagnose', ''),
                'Traitement': diagnosis_data.get('Traitement', ''),
                'InfoTraitement': diagnosis_data.get('InfoTraitement', ''),
                'AdviseTraitement': diagnosis_data.get('AdviseTraitement', ''),
                'AdviseGeneral': diagnosis_data.get('AdviseGeneral', ''),
                'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
            }
            
            # Génération du PDF
            pdf = render_to_pdf('../../core/templates/pdfReport.html', pdf_context)
            
            if pdf:
                with open(report_path, 'wb') as f:
                    f.write(pdf.content)
                print("PDF généré avec succès")
            else:
                print("Erreur lors de la génération du PDF")
            
            # Préparation des données pour l'affichage
            context = {
                'patient': patient_data,
                'diagnosis': diagnosis_data,
                'report_path': f'/patients/download-pdf/{report_filename}',
                'missing_data': missing_data
            }
            
            # Rendu du template
            html = render_to_string('patients/diagnosis_result.html', context)
            
            return JsonResponse({
                'html': html,
                'report_path': context['report_path'],
                'missing_data': missing_data
            })
            
        except Exception as e:
            print("Erreur dans get_diagnosis:", str(e))
            return JsonResponse({
                'error': f'Erreur lors de la génération du diagnostic: {str(e)}'
            }, status=500)
    
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def download_pdf(request, filename):
    """
    Télécharge le fichier PDF généré
    """
    try:
        file_path = os.path.join(settings.MEDIA_ROOT, 'reports', filename)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
        else:
            return HttpResponse("Fichier non trouvé", status=404)
    except Exception as e:
        print("Erreur lors du téléchargement du PDF:", str(e))
        return HttpResponse("Erreur lors du téléchargement du PDF", status=500)
