from django.shortcuts import render
from .models import Train
# Create your views here.
def Main(request):
    trains = Train.objects.all()
    return render(request,'trainapp/index.html',{'trains':trains})