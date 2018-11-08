from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MenuListView.as_view(),name='menu_list'),
    # path('add/',views.CreateMenu.as_view(),name='add_menu'),
]
