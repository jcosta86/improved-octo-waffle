from django.contrib import admin

from .models import Team, Sport, Match


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'match_location',
        'match_date',
        'id_team_1',
        'id_team_2',
        'id_sport',
        'score_team_1',
        'score_team_2')


admin.site.register(Team, TeamAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Match, MatchAdmin)
