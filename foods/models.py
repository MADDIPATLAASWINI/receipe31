# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Receipe(models.Model):
    user=models.CharField(max_length=20)
    receipe_name=models.CharField(max_length=20)
    ingredients=models.CharField(max_length=20)
    process=models.CharField(max_length=20)
    image=models.FileField(upload_to='media/')
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receipe_name

