from django.contrib.auth import login
from django.shortcuts import  render, redirect

from neighborapp.models import Neighborhood
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, request
from .forms import UpdateProfileForm,UpdateUserForm,RegisterForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get['email']
            username = form.cleaned_data.get('username')

            messages.success(request,f'Account for {username} created,you can now login')
            return redirect('login')
        else:
            form = RegisterForm()
        return render(request,'django_registration/registration_form.html', {'form': form})

def index(request):
    all_hoods = Neighborhood.objects.all().order_by("location")
    return render(request,'index.html', {'all_hoods': all_hoods})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    args = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'editprofile.html', args)