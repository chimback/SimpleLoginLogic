from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='login'),
    path('signup/', views.signup, name='signup'),
    path('base/', views.base, name='home'),
]
