from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact
from myapp.models import Home
from myapp.models import Users

# Create your views here.
def home(request):
    context={}
    system=request.POST.get('system',None)
    context['system']=system
    return render(request,'home.html')

def book(request):
    return render(request,'book.html')  

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method =="POST":
        cash = request.POST['cash']

        return render(request, 'register.html', {'cash' : cash})
    else:
        print("Error on Connection.")

    return render(request, 'register.html')


def userRegister(request):
    if request.method =="POST":
        username=request.POST.get('username')
        email = request.POST.get('email')
        password=request.POST.get('password')

        users = Users()

        users.username = username
        users.email = email
        users.password = password

        users.save()
    else:
        print("Error on Connection.")
        
    return render(request,'login.html', request.POST.get('cash'))

def loginCheck(request):
    username = request.POST.get('username')

    users = Users.objects.all()

    print(" ")
    print(users)
    print(" ")

    return render(request, 'login.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # contact= contact(name=name, email=email, phone= phone, date=datetime.today())
        contact = Contact()

        contact.name=name
        contact.email = email
        contact.phone=phone

        contact.save()
    return render(request,'contact.html') 

def home(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # contact= contact(name=name, email=email, phone= phone, date=datetime.today())
        home = Home()

        home.name=name
        home.email = email
        home.phone=phone

        Contact.save()
    return render(request,'home.html') 