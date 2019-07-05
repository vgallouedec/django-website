from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import Country
from django.utils import timezone

def index(request):
    russia = Country(name="France",date=timezone.now())
    russia.save()
    return HttpResponse("Hi, world. You're at the app index.")

def list(request):
    pays = Country.objects.all()
    return render(request,'index.html',{"pays":pays})

def backend(request):
    context = {}
    context['ajout'] = False
    if request.method == 'POST':
        pays = request.POST.get("pays","")
        newPays = Country(name=pays, date=timezone.now())
        newPays.save()
        context['ajout'] = True
    return render(request, 'backend.html',context)

