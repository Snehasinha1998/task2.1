from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('signup', views.signup, name='signup'),
    url('login', views.login_view, name='login'),
    url('dashboard', views.dashboard, name='dashboard'),
    url('Submit', views.submit_view, name='submit'),
] 