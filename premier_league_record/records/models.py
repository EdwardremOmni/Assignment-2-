from django.db import models

class Match(models.Model):
    code = models.BigIntegerField(unique=True)
    event = models.IntegerField()
    finished = models.BooleanField(default=False)
    finished_provisional = models.BooleanField(default=False)
    kickoff_time = models.DateTimeField()
    minutes = models.IntegerField()
    provisional_start_time = models.BooleanField(default=False)
    started = models.BooleanField(default=False)
    team_a = models.IntegerField()
    team_a_score = models.IntegerField()
    team_h = models.IntegerField()
    team_h_score = models.IntegerField()
    stats = models.JSONField()
    team_h_difficulty = models.IntegerField()
    team_a_difficulty = models.IntegerField()
    pulse_id = models.BigIntegerField()

    def __str__(self):
        return f"Match {self.code} (Event {self.event})"
