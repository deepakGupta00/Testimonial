from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request , 'layout.html')

@login_required(login_url='login/')
def home(request):
    return redirect('/dashboard/')
    # return render(request, 'auth/index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        return render(request, 'auth/login.html')
    
def sign_out(request):
    del request.session['user_data']
    return redirect('login')

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login') 