from django.contrib import messages
from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Library
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
           user = User.objects.create_user(username=name,email=email,password=password1)
           user.save()
           messages.success(request,'your account has been successfuly created!')
           return redirect('Login')
        else:
            messages.warning(request,'Password missmatching!!!')
            return redirect('Register')

    else:
        form = CreateUserForm()
    return render(request,'register.html',{'form':form})
# def login_page(request):
#     form = login_form()
#     if request.method == 'POST':
#         form = login_form(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=name,password=password)
#             if user is not None:
#                login(request,user)
#                return redirect('/')
#             else:
#                 messages.error(request,'incorrect username or password')
#                 return redirect('Login')
#         else:
#             form = login_form()
#     return render(request,'login.html',context={'form':form})   
@login_required
def profile(request):
    return render(request,'profile.html')
def lib_view(request):
    lib = Library.objects.all()
    return render(request,'home.html',{"lib":lib})