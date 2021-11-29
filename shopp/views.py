from django.shortcuts import render
from .models import shpping
def shopping (request):
    a=shpping.objects.all()
    return render(request,'index.html',{'a':a})
# Create your views here.
