from django.shortcuts import render

# Create your views here.
def webauto(request):
    return render(request,'webauto.html')

def index(request):
    return render(request,'index.html')