from django.contrib.auth.models import User 
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title','text',)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)