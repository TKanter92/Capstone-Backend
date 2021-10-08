from django.db import models
from django.contrib.auth.models import User

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patterns = models.BooleanField(default=False)
    textures = models.BooleanField(default=False)
    colors = models.CharField(max_length=20, default="none")
    molding = models.CharField(max_length=20, default="none")
    wallpaper = models.BooleanField(max_length=20, default="none")
    window_treatments = models.CharField(max_length=20, default="none")
    rugs = models.BooleanField(default=False)
    carpeting = models.BooleanField(default=False)
    budget = models.IntegerField(default=0)
