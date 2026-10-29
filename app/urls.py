from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_view),
    path('procurment/', procurment_view),
    path('management/', management_view),
    path('community/', community_view),
    path('documentation/', documentation_view),
]