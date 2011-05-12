from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

# Create your models here.

class Group(models.Model):
	group = models.CharField(max_length=1)
	def __unicode__(self):
		return self.group

class Team(models.Model):
	team = models.CharField(max_length=20)
	group = models.ForeignKey(Group)
	def __unicode__(self):
		return self.team

class Match(models.Model):
	group = models.ForeignKey(Group, null=True,blank=True)
	team_a = models.ForeignKey(Team, related_name='host')
	team_b = models.ForeignKey(Team, related_name='guest')
	date   = models.DateTimeField(null=True,blank=True)
	result_a = models.IntegerField(max_length=2,null=True,blank=True)
	result_b = models.IntegerField(max_length=2,null=True,blank=True)
	def __unicode__(self):
		return self.team_a.team +' - '+ self.team_b.team

class Guess(models.Model):
	match = models.ForeignKey(Match)
	guess_a = models.IntegerField(max_length=2)
	guess_b = models.IntegerField(max_length=2)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return str(self.guess_a) +' - '+ str(self.guess_b) + ' ('+self.match.team_a.team+' vs '+self.match.team_b.team+')'

class GuessForm(ModelForm):
	class Meta:
		model = Guess
		fields =('guess_a', 'guess_b')
		widgets = {
			'guess_a': TextInput(attrs={ 'size':'2', 'max_length':'2' }),
			'guess_b': TextInput(attrs={ 'size':'2', 'max_length':'2' }),
		}
