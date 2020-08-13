from django import forms
from .models import Post, CustomUser, Comment, Hashtag, Myinfo

#from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'location', 'hashtag_field']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname', 'phone_number']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']