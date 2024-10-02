from django.shortcuts import render,redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import CystomUserCreationForm
# Create your views here.
def profilesview(request):
    users = Profile.objects.all()
    context = {
        "users":users
    }
    return render(request,'users/profiles.html',context)
def profileview(request,id):
    user = Profile.objects.get(id=id)
    context = {
        'user':user
    }   
    return render(request,'users/profile.html',context)



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if all([username,password]):
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Tizimga muvaffaqiyatli kirildi')
                return redirect('/')
            else:
                messages.error(request,'Tizimga xatolik yuz berdi!')
    return render(request,'users/login.html')

def logout_user(request):
    try:
        logout(request)
        messages.success(request,'Tizimdan muvaffaqiyatli chiqildi!')

    except:
        messages.error(request,'Tizimdan muvaffaqiyatli chiqildi')

    return redirect('users:login')

def register_user(request):
    form = CystomUserCreationForm()
    for f in form:
        if f.label=='Password':
            f.label = 'Parol'
        elif f.label=='Password confirmation':
            f.label = 'Parolni Tasdiqlash'
    context = {
        "form":form
    }

    if request.method == "POST":
        form = CystomUserCreationForm(request.POST)
        for f in form:
                if f.label == "Password":
                    f.label = "Parol"
                elif f.label == "Password confirmation":
                    f.label = "Parolni tasdiqlash"

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            messages.success(request,'Tizimdan muvaffaqiyatli royxatdan ottiz!')
            return redirect('/')
        else:
            messages.error(request,'Tizimga xatolik yuz berdi!')

    return render(request,'users/register.html',context)