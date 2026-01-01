from django.shortcuts import render
from .models import *
import json

# Create your views here.

def index(request):
    return render(request, "main.html")

def gm_dashboard(request):
    return render(request, "main.html", context={'tipo':'GAME MASTER'})

def player_view(request):
    return render(request, "main.html", context={'tipo':'PLAYER'})