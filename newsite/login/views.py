from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('base')
        else:
        # Return an 'invalid login' error message.
            messages.success(request, ("There was an error. Please Try Again :("))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out Successfully!"))
    return redirect('login')

def signup_user(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return(redirect, 'login')
        else:
            messages.success(request, "There Was An Error Registering. Try Again...")
            return redirect('register_user')
            form = UserCreationForm()
    return render(request, 'authenticate/signup.html', {
        'form':form,
    })
    
def home(request):
    return render(request, 'authenticate/home.html',{})
