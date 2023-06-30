from django.db import models

# Create your models here.
title=models.CharField(max_length=50)
print(title)
class Task(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    time=models.TimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title