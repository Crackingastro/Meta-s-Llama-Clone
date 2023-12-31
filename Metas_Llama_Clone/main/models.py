from django.db import models

# Create your models here.
class question(models.Model):
    ques = models.CharField(max_length=2000)

    def __str__(self):
        return self.ques

class answer(models.Model):
    ans = models.CharField(max_length=3000)

    def __str__(self):
        return self.ans