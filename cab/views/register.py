from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth 
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.template import RequestContext

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(render_value=False))
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is already in use.Please choose another.")
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("You must type the same password each time")
            return self.cleaned_data
    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                                email=self.cleaned_data['email'],
                                                password=self.cleaned_data['password1'])
        return new_user

    
def sighup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = SignupForm()
    return render_to_response('signup.html',
                                       ,add_csrf(request,{'form':form}))
def login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('cab_snippet_list'))
            else:
                pass
    return render_to_response('login.html',add_csrf(request))
            
def add_csrf(request,kwargs={}):
    d=dict(kwargs)
    d.update(csrf(request))
    return d
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('cab_snippet_list'))
