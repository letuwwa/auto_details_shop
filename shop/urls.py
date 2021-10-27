from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.details_by_category, name='category'),
    path('detail/<int:detail_id>/', views.detail_single, name='detail'),
    path('about-us/', views.about_us, name='about-us'),
]
