from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User,auth 
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import SignupForm, loginForm, donateForm
from .models import DonateDetail
from django.shortcuts import render
from django.http import HttpResponse
# import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def Home(request):
    return render(request,"index.html",{
        'form':loginForm, 'form2':SignupForm
    })
def signup(request):
    if request.method == 'POST':
        user = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(email=email).exists():
            return redirect('index')
            return HttpResponseRedirect("Email exist")
                    
        else:
                user = User.objects.create_user(username=user, password=password2, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request,"index.html",{
                    'form':loginForm,'form2':SignupForm
                })  
    else:
        return render(request,"index.html",{
            'form':loginForm, 'form2':SignupForm
        })


def About(request):
    return render(request, "About.html")

def Gallery(request):
    return render(request, "Gallery.html")
def Donate(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Amount = int(request.POST.get('Amount'))
        form4 = donateForm(request.POST)
        return render(request,"donate1.html",{
            'name':Name,'price':Amount*100,'Amount':Amount,'form4':form4
        })
        
    else:
        return render(request,"Donate.html",{
            'form3':donateForm
        })
def donate1(request):
    if request.method=='POST':
        
        form= donateForm(request.POST)
        if form.is_valid:
            name = request.POST['Name']
            price = request.POST['Amount']  
            Amount = price*100
            client = razorpay.Client(auth=("rzp_test_7mulrpNkoezekp", "NtnT3yTP29xWAibECp4uvB0b"))
            payment = client.order.create({'amount':Amount, 'currency': 'INR'})              
            obj = DonateDetail(name=name, Amount=price)
            obj.save()
            return render(request,"success.html")
        else:
            return render(request,"donate1.html",{
                'form4':form
            })
    else:
        form4= donateForm(request.POST)
        return render(request,"donate1.html",{
            'form4':form4
        })

@csrf_exempt
def success(request):
    return render(request, "success.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"index.html")
    else:
        return render(request, "index.html", {
            'form3':loginForm, 'form2':SignupForm
        })
def logout(request):
    auth.logout(request)
    return render(request,"index.html",{
        'form':loginForm,'form2':SignupForm
    })
def logedin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST["password"]
        new_password = request.POST["new_password"]
        con_password =request.POST["confirm_password"]
        if new_password == con_password:
            user = authenticate(username=username, password=password)
            if user is not None:
                user.set_password(con_password)
                user.save()
                return render(request,"logedin.html")
            else:
                
                messages.info(request,"Password Incorect.") 
                return redirect('logedin')
        else:
            messages.info(request,"New password and confirm password didn't match")
            return render(request,'logedin')
    else:
        return render(request,"logedin.html")