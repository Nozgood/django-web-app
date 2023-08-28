from django.urls import path
from listings import views

# SERT A DECLARER L'APPLICATION
app_name = "listings"

urlpatterns = [
    path('bands/', views.band_list, name="band_list"),
    path('bands/<int:band_id>/', views.band_detail, name='band_detail'),
    path('about/', views.about_us),
    path('contact/', views.contact_us, name="contact"),
    path('listings/', views.listings),
    path('', views.home)
]