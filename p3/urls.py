"""p3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from p3 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="sam"),
    path('home',views.home,name="aadi"),
    path('html1',views.html1,name="html"),
    path('html2',views.html2,name="html2"),
    path('html3',views.html3,name="html3"),
    path('html4',views.html4,name="html4"),
]
