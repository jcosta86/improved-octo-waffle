from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Match(models.Model):
    match_location = models.CharField(max_length=100)
    id_team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='+')
    id_team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, related_name='+')
    id_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=False)
    match_date = models.DateTimeField(null=False)
    score_team_1 = models.IntegerField(default=0)
    score_team_2 = models.IntegerField(default=0)

    def __str__(self):
        return f"Match location: {self.match_location} Date: {self.match_date}"
