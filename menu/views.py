from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                    DetailView,UpdateView,
                                    DeleteView,CreateView)
from . models import Menu
from . forms import MenuForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class MenuListView(ListView):
    model = Menu
    context_object_name = 'menu_list'

class CreateMenu(LoginRequiredMixin,CreateView):
    model = Menu
    form_class = MenuForm
