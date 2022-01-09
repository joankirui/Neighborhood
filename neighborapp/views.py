from django.contrib.auth import login
from django.shortcuts import  get_object_or_404, render, redirect
from neighborapp.models import Business, Neighborhood, Post, Profile
from .forms import BusinessForm, NeighbourHoodForm, PostForm, RegisterForm
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
@login_required(login_url='/accounts/login/')
def index(request):
    all_hoods = Neighborhood.objects.all().order_by("location")
    return render(request,'index.html', {'all_hoods': all_hoods})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def hood_members(request,hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighborhood=hood)

    return render(request, 'members.html',{'members': members} )

@login_required(login_url='/accounts/login/')
def newhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')

    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html' ,{'form': form})

@login_required(login_url='/accounts/login/')
def make_post(request,hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html',{'form': form})

@login_required(login_url='/accounts/login/')
def single_hood(request,hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(hood=hood)
    
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            bform = form.save(commit=False)
            bform.hood = hood
            bform.user = request.user.profile
            bform.save()
            return redirect('single-hood', hood.id)
        
    else:  
        form = BusinessForm()
    args = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts,
    }
    return render(request, 'singlehood.html',args) 

@login_required(login_url='/accounts/login/')
def join_hood(request, id):
    neighborhood = get_object_or_404(Neighborhood,id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def leave_hood(request, id):
    hood = get_object_or_404(Neighborhood,id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def search_business(request):

    if 'email' in request.GET and request.GET["email"]:
        search_term = request.GET.get("email")
        results = Business.search_by_email(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"results":results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})