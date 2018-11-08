from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.CreateTable.as_view(),name='book_table'),
    path('userlist/',views.TableListView.as_view(),name='table_user_list'),
    path('book/confirm/',views.MailSent.as_view(), name='confirm-mail')
]
