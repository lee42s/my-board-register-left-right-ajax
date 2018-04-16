"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView
from mysite.views import UserRegisterView, UserRegisterDoneView

from mysite import views
from leftright.views import getpoint

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserRegisterDoneView.as_view(), name='register_done'),
    # ajax 는 ajax/로 시작하여 구분합니다.
    url(r'^ajax/validate_username/$', views.validate_username, name="validate_username"),
    url(r'^ajax/leftright_getpoint/$', getpoint, name="leftright_getpoint"),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^game/', include('leftright.urls', namespace='game')),
]
