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
from django.urls import path , include
from tools.views import Team , ShowTooLS , Showitem ,ShowTooLSog ,CreatNewTool , toolsapi,UpdateNewTool ,DeleteNewTool
from accounts.views import CreatNewUser,user_login ,user_log_out 
from django.conf.urls.i18n import i18n_patterns


urlpatterns =[
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('team/',Team.as_view(),name='team'),
    path('list-show/<slug:slug>/',Showitem.as_view(),name='item'),
    path('list/create/',CreatNewTool.as_view(),name='create'),
    path('list/<slug:slug>/',UpdateNewTool.as_view(),name='update'),
    path('list/<slug:slug>/delete/',DeleteNewTool.as_view(),name='delete'),
    path('aa/',ShowTooLS.as_view(),name='list'),
    path('',ShowTooLSog.as_view(),name='list'),
    path('register/' , CreatNewUser.as_view() , name='register'),
    path('login/' , user_login , name='login'),
    # path('user-update/' , UpdateUser.as_view() , name='updateuser'),
    path('logout/' , user_log_out , name='logout'),
    path('api/tools', toolsapi , name='tools')
)
