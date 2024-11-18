from django.shortcuts import render, redirect,HttpResponse
from .models import receita

def home(request):
    rece = receita.objects.all()
    if request.method == 'POST':
        item = request.POST.get('ingredientes_usu')
        
        
        
    return render(request, 'home.html')