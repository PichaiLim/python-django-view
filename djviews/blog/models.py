# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return [
            self.first_name,
            self.last_name
        ]

class SeialNumber(models.Model):
    running_number = models.CharField(max_length=30)
    # person_id = models.OneToOneField(Person, thorugh='Membership')
    # person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.running_number