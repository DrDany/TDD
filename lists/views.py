from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Создайте здесь представления свои.
def home_page(request):
    return render(request, 'home.html')

'''домашняя страница'''
