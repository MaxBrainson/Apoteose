from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime

class ReportGenerator:
    def __init__(self, patient_data, diagnosis_data):
        self.patient_data = patient_data
        self.diagnosis_data = diagnosis_data
        self.styles = getSampleStyleSheet()
        self.custom_style = ParagraphStyle(
            'CustomStyle',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=10
        )
        self.title_style = ParagraphStyle(
            'TitleStyle',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=20
        )

    def generate_patient_summary(self):
        """Génère la section résumé patient"""
        elements = []
        elements.append(Paragraph("Résumé Patient", self.title_style))
        
        patient_info = [
            ["Nom", self.patient_data["nom"]],
            ["Prénom", self.patient_data["prenom"]],
            ["Âge", str(self.patient_data["age"])],
            ["Sexe", self.patient_data["sexe"]],
            ["IMC", str(self.patient_data["imc"])]
        ]
        
        t = Table(patient_info, colWidths=[2*inch, 4*inch])
        t.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        
        elements.append(t)
        elements.append(Spacer(1, 20))
        return elements

    def generate_diagnosis_section(self):
        """Génère la section diagnostic"""
        elements = []
        elements.append(Paragraph("Résultats et Diagnostic", self.title_style))
        
        scores_info = [
            ["Score", "Valeur", "Classification"],
            ["T-Score", str(self.diagnosis_data["t_score"]), self.diagnosis_data["t_score_class"]],
            ["Z-Score", str(self.diagnosis_data["z_score"]), self.diagnosis_data["z_score_class"]]
        ]
        
        t = Table(scores_info, colWidths=[2*inch, 2*inch, 2*inch])
        t.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        
        elements.append(t)
        elements.append(Spacer(1, 20))
        
        # Diagnostic final
        elements.append(Paragraph("Diagnostic Final", self.styles['Heading2']))
        elements.append(Paragraph(self.diagnosis_data["final_diagnosis"], self.custom_style))
        
        return elements

    def generate_risk_factors(self):
        """Génère la section facteurs de risque"""
        elements = []
        elements.append(Paragraph("Facteurs de Risque", self.title_style))
        
        risk_factors = self.diagnosis_data["risk_factors"]
        
        # Facteurs majeurs
        elements.append(Paragraph("Facteurs Majeurs:", self.styles['Heading2']))
        for factor in risk_factors["majeurs"]:
            elements.append(Paragraph(f"• {factor}", self.custom_style))
        
        elements.append(Spacer(1, 10))
        
        # Facteurs mineurs
        elements.append(Paragraph("Facteurs Mineurs:", self.styles['Heading2']))
        for factor in risk_factors["mineurs"]:
            elements.append(Paragraph(f"• {factor}", self.custom_style))
        
        elements.append(Spacer(1, 20))
        return elements

    def generate_recommendations(self):
        """Génère la section recommandations"""
        elements = []
        elements.append(Paragraph("Recommandations", self.title_style))
        
        recommendations = self.diagnosis_data["recommendations"]
        
        # Recommandations générales
        elements.append(Paragraph("Recommandations Générales:", self.styles['Heading2']))
        for rec in recommendations["générales"]:
            elements.append(Paragraph(f"• {rec}", self.custom_style))
        
        elements.append(Spacer(1, 10))
        
        # Recommandations spécifiques
        if recommendations["spécifiques"]:
            elements.append(Paragraph("Recommandations Spécifiques:", self.styles['Heading2']))
            for rec in recommendations["spécifiques"]:
                elements.append(Paragraph(f"• {rec}", self.custom_style))
        
        return elements

    def generate_report(self, output_path):
        """Génère le rapport PDF complet"""
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        elements = []
        
        # Ajout de la date
        elements.append(Paragraph(f"Rapport généré le {datetime.now().strftime('%d/%m/%Y')}", self.styles['Normal']))
        elements.append(Spacer(1, 20))
        
        # Ajout des différentes sections
        elements.extend(self.generate_patient_summary())
        elements.extend(self.generate_diagnosis_section())
        elements.extend(self.generate_risk_factors())
        elements.extend(self.generate_recommendations())
        
        # Génération du PDF
        doc.build(elements) 