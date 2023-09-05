from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('vector/', views.vector, name='vector'),
    path('logos/', views.logos, name="logos"),
    path('pixel/', views.pixel, name="pixel"),
    path('ui_ux/', views.ui_ux, name="ui_ux"),
    path('general/', views.general, name="general")
]