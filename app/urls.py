from django.urls import path
from . import views

urlpatterns = [
    path('', index.views, name="index"),
    path('jogadores/', jogadores.views, name="jogadores"),
    path('sobre/', sobre.views, name="sobre"),
]