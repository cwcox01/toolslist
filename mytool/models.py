from django.db import models
from django.shortcuts import render

# Create your models here.


class Tool(models.Model):
    brand = models.CharField(default="", max_length=20, blank=False)
    tool_type = models.CharField(default="", max_length=20, blank=False)
    cordless = models.CharField(default="yes",
                                max_length=4,  blank=False)
    voltage = models.IntegerField()
    brushless = models.CharField(
        default="yes", max_length=4,)
    quantity = models.IntegerField(default=0, blank=False)
    description = models.CharField(default="", max_length=150)


class Battery(models.Model):
    brand = models.CharField(default="", max_length=20, blank=False)
    voltage = models.IntegerField(default=1, blank=False)
    amperage = models.DecimalField(
        default=0, max_digits=2, decimal_places=1, blank=False)
    HIGH_PERFORMANCE = [("Y", "Yes"), ("N", "No")]
    performance_choice = models.CharField(default="",
                                          max_length=1, help_text="Select yes if high performance battery.", choices=HIGH_PERFORMANCE)
    quantity = models.IntegerField(default=0, blank=False)
    description = models.CharField(default="", max_length=150)
