from django.shortcuts import render
from django.http import HttpResponse
from django.http import  HttpRequest
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list(string.ascii_lowercase)
    if request.GET.get('capitalletters'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('specialcharacters'):
        characters.extend(list("!£$%^&*()_+=-`<>/#@:~};'[]"))
    
    print(characters)
    
    thepassword=''
    length = int(request.GET.get("Length"))
    
    for x in range(length):
        random.shuffle(characters)
        thepassword = thepassword + characters[1]
    
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')