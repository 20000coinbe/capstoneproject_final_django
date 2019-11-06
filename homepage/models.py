from django.db import models
from django.urls import reverse

# Create your models here.

class Serach(models.Model):
    word = models.CharField(max_length=50, help_text="검색할 내용을 입력하시오")

    def __str__(self):
        return self.name

    