from django.shortcuts import render
from django.views.generic import  ListView, DetailView, CreateView,DeleteView,UpdateView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView): 
  template_name = 'snacklist.html'
  model = Snack

class SnackDetailView(DetailView): 
  template_name = 'snackdetail.html'
  model = Snack

class SnackCreateView(CreateView): 
  template_name = 'snackcreate.html'
  model = Snack
  fields = ['title', 'description', 'purchaser']
  success_url = reverse_lazy("snacklist")

class SnackDeleteView(DeleteView): 
  template_name = 'snackdelete.html'
  model = Snack
  success_url = reverse_lazy("snacklist")


class SnackUpdateView(UpdateView): 
  template_name = 'snackupdate.html'
  model = Snack
  fields = ['title', 'description', 'purchaser']
  success_url = reverse_lazy("snacklist")