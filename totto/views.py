# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import SimpleTemplateResponse
from totto.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from forms import RegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages


def index(request):
	return SimpleTemplateResponse('totto/index.html')

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return render_to_response("totto/complete.html")
	else:
		form = RegisterForm()
	
	return render_to_response("totto/register.html", {'form': form, },
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
				return HttpResponseRedirect("groups/")
			else:
				messages.add_message(request, messages.INFO, 'Konto gesperrt')

		else:
			messages.add_message(request, messages.INFO, 'Username oder Passwort falsch')

	elif	request.user.is_authenticated():
		return HttpResponseRedirect("/totto/groups/")

	else:
		form = AuthenticationForm()
	
	return render_to_response("totto/index.html", {'form': form,},
								context_instance=RequestContext(request))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect("/totto/login")

@login_required()
def groups(request):
	user = request.user
	group = 0
	groups = Group.objects.all()
	teams = Team.objects.all()
	for team in teams:
		teams.append = [
			{'team': team, 'group': group}
		]
	return render_to_response("totto/groups.html", {'groups': groups, 'teams': teams, 'user': user })
	

@login_required()
def group(request, group_id):
	group = group_id
	groupmatches = Match.objects.filter(group=group)
	allguesses = Guess.objects.filter(user=request.user.id)

	if request.method == 'POST':

		form = GuessForm(request.POST)
		if form.is_valid():

			user = request.user.id
			match = request.POST['match']
			guess_a = request.POST['guess_a']
			guess_b = request.POST['guess_b']
			g = Guess(match_id=match, guess_a=guess_a, guess_b=guess_b, user_id=user)
		


			if Guess.objects.filter(match=match, user=user):
				guess_id = Guess.objects.get(match=match, user=user).id
				Guess(id=guess_id, guess_a=guess_a, guess_b=guess_b, match_id=match, user_id=user).save()
				messages.add_message(request, messages.INFO, 'Tipp aktualisiert')
			else:
				g.save()
				messages.add_message(request, messages.INFO, 'Tipp gespeichert')
			return render_to_response('totto/group.html', {'groupmatches': groupmatches, 'group': group, 'allguesses': allguesses, 'match': match, 'form': GuessForm(),},
															context_instance=RequestContext(request))

	else:
		form = GuessForm()
	return render_to_response('totto/group.html', {'groupmatches': groupmatches, 'group': group, 'allguesses': allguesses, 'form': form,},
															context_instance=RequestContext(request))

@login_required()
def detail(request, match_id):
	team_a = str(Match.objects.get(pk=match_id).team_a)
	team_b = str(Match.objects.get(pk=match_id).team_b)
	teams = team_a +' - '+ team_b
	return HttpResponse("%s" % teams)
