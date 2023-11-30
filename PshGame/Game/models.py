from django.db import models

# Create your models here.
class GameStatistic(models.Model):
    player_id = models.CharField(max_length=10)
    nickname = models.CharField(max_length=50)
    profile_image = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
