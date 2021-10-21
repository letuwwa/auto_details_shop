from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.details_by_category, name='category'),
]
