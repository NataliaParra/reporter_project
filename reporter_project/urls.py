"""reporter_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from reporter.views import home
from reporter import urls as reporter_urls



urlpatterns = [     
         #P<num> son los parametros                
    url(r'^(?P<num1>\d+)/(?P<num2>\d+)$',home, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^galleta/', include(reporter_urls))
    
]
