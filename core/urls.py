from django.urls import path
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.home, name='HomePage'),
    path('count/', views.count, name='CountPage'),
]
