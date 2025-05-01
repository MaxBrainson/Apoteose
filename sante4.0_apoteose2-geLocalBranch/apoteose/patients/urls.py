from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('form/', views.form, name='form'),
    path('diagnosis/', views.get_diagnosis, name='diagnosis'),
    path('download-pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    # ... autres URLs existantes ...
] 