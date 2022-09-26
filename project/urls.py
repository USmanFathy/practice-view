"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tools.views import Team , ShowTooLS , Showitem ,ShowTooLSog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/',Team.as_view(),name='team'),
    path('list/<int:id>',Showitem.as_view(),name='item'),
    path('list/',ShowTooLS.as_view(),name='list'),
    path('listview/',ShowTooLSog.as_view(),name='list'),
]
