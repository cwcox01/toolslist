from django.db import models

# Create your models here.


class Tools(models.Model):
    brand = models.CharField(max_length=20, blank=False),
    tool_type = models.CharField(max_length=20, blank=False),
    CORDLESS = [("Y", "Yes"),
                ("N", "No"),
                ],
    cordless_type = models.CharField(
        max_length=1, choices=CORDLESS, blank=False),
    voltage = models.IntegerField(),
    BRUSHLESS = [("Y", "Yes"),
                 ("N", "No"),
                 ],
    brushless_type = models.CharField(max_length=1, choices=BRUSHLESS),
    quantity = models.IntegerField(),
    description = models.CharField(max_length=150),


class Batteries(models.Model):
    brand = models.CharField(max_length=20, blank=False),
    voltage = models.IntegerField(blank=False),
    amp_hours = models.IntegerField(blank=False),
    HIGH_PERFORMANCE = [("Y", "Yes"),
                        ("N", "No"),
                        ],
    performance_choice = models.CharField(
        max_length=1, choices=HIGH_PERFORMANCE),
    quantity = models.IntegerField(blank=False),
    description = models.CharField(max_length=150),
