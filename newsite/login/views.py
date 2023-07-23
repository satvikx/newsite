from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('projects')
        else:
        # Return an 'invalid login' error message.
            messages.success(request, 'There was an error. Please Try Again :(')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('login')

def signup_user(request):
    # form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username = username, password = password1)
            # login(request, user)
            # messages.success(request, ("Registration Successful!"))
            return redirect('login')
        else:
            messages.success(request, "There Was An Error Registering. Try Again...")
            form = RegisterUserForm()
            return redirect('signup')
    return render(request, 'authenticate/signup.html', {'form' : form})

def signup_userr(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password1)
        data.save()
        return redirect('login')
    return render(request, 'authenticate/signup.html')
    
def home(request):
    return render(request, 'projects/projects.html',{})

def is_notvalid(request):
    messages.success(request, "Try Logging In First...")
    #return render(request, 'authenticate/login.html', {})
    return HttpResponseRedirect('/login')

