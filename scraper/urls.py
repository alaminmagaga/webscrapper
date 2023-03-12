from django.urls import path
from . import views

urlpatterns = [
            path('', views.home, name='home'),
            path('scrape/', views.scrape, name='scrape'),
            path('download/', views.download_file, name='download_file'),
        ]
        