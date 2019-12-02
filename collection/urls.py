from django.urls import path
from collection.views import GameIndexView, EditMenuView
from django.conf import settings

urlpatterns = [
    path('<game>/', GameIndexView.as_view(), name='game-index'),
    path('<game>/editmenu/', EditMenuView.as_view(), name='edit-collection-menu')
] 
