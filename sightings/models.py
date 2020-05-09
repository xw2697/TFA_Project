from django.db import models

# Create your models here.
class Squirrel(models.Model):
    CHOICES_SHIFT = (
        ('am','AM'),
        ('pm','PM'),
    )
    CHOICES_AGE = (
        ('adult','Adult'),
        ('juvenile','Juvenile'),
    )

    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    unique_Squirrel_ID = models.CharField('Unique_Squirrel_ID',max_length=50)
    shift = models.CharField('Shift',max_length=50, choices=CHOICES_SHIFT)
    date = models.dateField('Date')
    age = models.CharField('Age',max_length=50, choices=CHOICES_AGE)
from django.db import models

# Create your models here.
