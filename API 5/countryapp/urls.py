
from django.urls import path
from . import views
urlpatterns = [
    path('', views.country_search, name='country_search'),
    path('country/<str:country_name>/', views.country_detail, name='country_detail'),
]