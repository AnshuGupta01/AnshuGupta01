from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash


#Home view Function
def home(request):
    return render(request,'authentication/home.html')

# Signup View Function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!')
            fm.save()
    else:        
     fm = SignUpForm()
    return render(request,"signup.html",{'form':fm})
    
#login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!')
                    return HttpResponseRedirect('/base/')
        else:
            fm = AuthenticationForm()
        return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/base/') 

#Base
def user_profile(request):
    if request.user.is_authenticated:
      return render(request , 'authentication/base.html' ,{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

#Logout View Function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#Change Password with old Password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data =request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request ,fm.user )
                messages.success(request, 'Password Changed Successfully!!')
                return HttpResponseRedirect('/base/')
        else:   
            fm =PasswordChangeForm(user=request.user)
        return render(request,'authentication/changepass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/error/')