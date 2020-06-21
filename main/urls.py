"""intenseSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .  import views

app_name = "main"
urlpatterns = [
	path('',views.homepage , name = "homepage"),
	path('about.html' ,views.about , name = "about"),
	path('Enquiry', views.employer, name = "employer"),
	path('Partner', views.partner, name = "partner"),
    path('Contact', views.contact_us, name = "contact"),
    path('log_sign.html',views.log_sign , name= "log_sign"), 
    path("candidate.html", views.candidate, name='candidate'), 
    path("jobs.html", views.jobs, name='jobs'), 
    path("apply.html", views.apply, name='apply'), 
    path("patcomm.html", views.apply, name='patcomm'), 

  
]
