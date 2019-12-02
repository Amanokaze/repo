from django.urls import path
from main.views import *
from django.conf import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-request/', AddRequestView.as_view(), name='add-request'),
    path('sidebar-games/', SidebarGamesView.as_view(), name='sidebar-games'),
] 
