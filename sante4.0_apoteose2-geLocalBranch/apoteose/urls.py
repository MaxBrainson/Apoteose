from django.contrib import admin
from django.urls import path, include

import apoteose.core.views
import apoteose.patients.views
import apoteose.doctors.views

urlpatterns = [
    path('', apoteose.core.views.loading),
    path('home/', apoteose.core.views.home, name = 'home'),
    path('form/', apoteose.patients.views.form, name = 'form'),
    path('login/', apoteose.doctors.views.login, name = 'login'),
    # path('pdf-report/', apoteose.patients.views.download_pdf, name='pdf-report'),
    path('admin/', admin.site.urls),
]
