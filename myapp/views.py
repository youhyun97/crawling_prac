from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def home(request):
    return render(request, 'home.html')
