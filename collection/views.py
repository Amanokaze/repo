from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from collection.models import GrGameCollections

# Create your views here.
class GameIndexView(TemplateView):
    template_name = 'game_index.html'

class EditMenuView(ListView):
    model = GrGameCollections
    template_name = 'edit_menu.html'

    def get_queryset(self):
        collection = GrGameCollections.objects.filter(game__code=self.kwargs['game'])
        return collection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.kwargs['game']
        return context