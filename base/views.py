from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

# Create your views here.

def welcome_view(request):
    return render(request, 'base/base.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})