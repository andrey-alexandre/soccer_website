from django.db import models

# Create your models here.
class Matches(models.Model):
    Data = models.DateTimeField()
    GameId = models.IntegerField(primary_key=True)
    Time = models.TextField()
    Local = models.TextField()
    TipoMetrica = models.TextField()
    JogosCasa = models.IntegerField()
    JogosFora = models.IntegerField()
    Goal_T1 = models.FloatField()
    Goal_T2 = models.FloatField()
    GoalOver_T1 = models.IntegerField()
    GoalOver_T2 = models.IntegerField()
    Corner_T1 = models.FloatField()
    Corner_T2 = models.FloatField()
    CornerOver_T1 = models.IntegerField()
    CornerOver_T2 = models.IntegerField()
    Win_T1 = models.TextField()
    Win_T2 = models.TextField()
    url = models.TextField()