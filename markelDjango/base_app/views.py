from socket import create_server
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Food

class FoodList(ListView): # using a Class based view, will return a template with a query set of data
    model = Food
    context_object_name = 'foods'

class FoodDetail(DetailView): # see a specific food
    model = Food
    context_object_name = 'food'
    template_name = 'base_app/food.html' # setting template name without the expected _detail prefitx

class FoodCreate(CreateView): # this will send a post request
    model = Food
    fields = '__all__'
    success_url = reverse_lazy('foods') # send user back to foods, which is specified as the url name in first url

class FoodUpdate(UpdateView):
    model = Food
    fields = '__all__'
    success_url = reverse_lazy('foods')   

class FoodDelete(DeleteView):
    model = Food
    context_object_name = 'food' #render by food itself not object
    success_url = reverse_lazy('foods')   
