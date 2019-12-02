from django.shortcuts import render
from django.views.generic import ListView, FormView
from main.models import GrGameCategories, GrGameMasters
from main.forms import AddRequestForm

# Create your views here.
class IndexView(ListView):
    model = GrGameMasters
    template_name = 'index.html'

class AddRequestView(FormView):
    template_name = 'add_request.html'
    form_class = AddRequestForm

class SidebarGamesView(ListView):
    model = GrGameMasters
    template_name = 'include/sidebar_games.html'

