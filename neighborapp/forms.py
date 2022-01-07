from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Neighborhood,Business

# Create your forms here.
class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.Enter a valid email address. ')

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['prof_pic', 'bio','contact','name','location','neighborhood']

class NeighbourHoodForm(forms.ModelForm):

    class Meta:
        model = Neighborhood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ('user', 'hood')