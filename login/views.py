from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.
def login_view(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to a home page or wherever
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})