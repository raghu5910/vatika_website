from django.shortcuts import render
from .models import BookTable, BookLawn
from django.views.generic import (TemplateView,ListView,CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookTableForm, BookLawnForm
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class CreateTable(LoginRequiredMixin, CreateView):
    model = BookTable
    form_class = BookTableForm

    def form_valid(self, form):
        table = form.save(commit=False)
        form.instance.booked_by = self.request.user
        send_mail('Village Vatiki','Hello, from Village Vatika.Your booking is confirmed','Raghu5910@outlook',['raghuram5910@gmail.com'],fail_silently=True)
        messages.success(self.request, f'Table booked for the {self.request.user}!')
        return super(CreateTable, self).form_valid(form)

class CreateLawn(LoginRequiredMixin, CreateView):
    model = BookLawn
    form_class = BookLawnForm
    template_name = 'Table/booklawn_form.html'

    def form_valid(self, form):
        table = form.save(commit=False)
        form.instance.booked_by = self.request.user
        send_mail('Village Vatiki','Hello, from Village Vatika.Your booking is confirmed','Raghu5910@outlook',['raghuram5910@gmail.com'],fail_silently=True)
        message.success(request, f'Table booked for the {self.request.user}!')
        return super(CreateLawn, self).form_valid(form)

class MailSent(TemplateView):
    template_name = 'Table/table_confirm_mail.html'



class TableListView(LoginRequiredMixin, TemplateView):
    template_name = 'Table/booking_list.html'

    def get(self, request):

        query1 = BookTable.objects.filter(booked_by=self.request.user).order_by('time')
        context = {'bookings':query1}
        return render(request, self.template_name, context)
