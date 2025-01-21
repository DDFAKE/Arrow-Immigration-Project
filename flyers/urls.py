"""flyers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


from re import template
from tracemalloc import Statistic
from typing import Generic
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from visa import views
from django.views.generic.base import TemplateView


urlpatterns = [
  
    path('admin', admin.site.urls),
    path('canada.html', views.showform,name='home'),
    path('usa.html', views.usa,name='home'),
    path('uk.html', views.uk,name='home'),
    path('gre.html', views.gre,name='home'),
    path('ielts.html', views.ielts,name='home'),
    path('toefl.html', views.toefl,name='toefl'),
    path('sat.html', views.sat,name='sat'),
    path('spokenenglish.html', views.spokenenglish,name='spokenenglish'),
    path('mainmenusave',views.mainmenusave,name='msave'),
    path('submenusave',views.submenusave,name='submenusave'),
    path('index',views.dynamic_menu,name='index'),
    path('country',views.country),
    path('visa',views.visa,name='visa'),
    path('work',views.work,name='work'),
    path('contact.html', views.contact, name='contact_us'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
