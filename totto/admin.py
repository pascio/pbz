from totto.models import Match,Guess,Team,Group
from django.contrib import admin

class MatchAdmin(admin.ModelAdmin):

	fieldsets = [
		('Group', 			{'fields': ['group']}),
		('Teams', 			{'fields': ('team_a','team_b')}),
		('Results',			{'fields': ('result_a','result_b')}),
		('Date information', {'fields': ['date']}),
	]
	list_display	= ('team_a', 'team_b', 'result_a', 'result_b')
	list_filter 	= ['group']
	ordering		= ['group']
admin.site.register(Match, MatchAdmin)

class GuessAdmin(admin.ModelAdmin):
	fields = ('match', 'guess_a', 'guess_b', 'user')
	list_display = ('match', 'guess_a', 'guess_b', 'user')
	list_filter = ('match', 'user')
admin.site.register(Guess, GuessAdmin)

class TeamAdmin(admin.ModelAdmin):
	fields = ('team', 'group')
	list_display = ('team', 'group')
admin.site.register(Team, TeamAdmin)

class GroupAdmin(admin.ModelAdmin):
	field = ('group')
admin.site.register(Group, GroupAdmin)
