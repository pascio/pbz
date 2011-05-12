# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import RegisterForm
from django.template import RequestContext

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = RegisterForm()
	
	return render_to_response("my_auth/register.html", {'form': form, },
								context_instance=RequestContext(request))

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return HttpResponseRedirect("/teams/")
			else:
				return HttpResponseRecirect("http://www.google.com")

		else:
			return HttpResponseRedirect("http://www.meteoschweiz.ch")
	else:
		form = AuthenticationForm()
	
	return render_to_response("my_auth/login.html", {'form': form, },
								context_instance=RequestContext(request))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/")
