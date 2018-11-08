from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePage.as_view(),name='home-page'),
    path('about/',views.AboutPage.as_view(), name = "about-page"),
]
