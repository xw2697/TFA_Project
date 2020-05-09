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
    CHOICES_FUR = (
        ('gray','Gray'),
        ('cinnamon','Cinnamon'),
        ('black','Black'),
    )
    CHOICES_LOCATION = (
        ('ground plane', 'Ground Plane'),
        ('above ground', 'Above Ground'),
    )
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')
    unique_Squirrel_ID = models.CharField('Unique_Squirrel_ID',max_length=50)
    shift = models.CharField('Shift',max_length=50, choices=CHOICES_SHIFT)
    date = models.dateField('Date')
    age = models.CharField('Age',max_length=50, choices=CHOICES_AGE)
    primary_Fur_Color = models.CharField('Primary_Fur_Color',max_length=50, choices=CHOICES_FUR)
    location = models.CharField('Location',max_length=50, choices=CHOICES_LOCATION)
    specific_Location = models.TextField('Specific_Location')
    running = models.BooleanField('Running')
    chasing = models.BooleanField('Chasing')
    climbing = models.BooleanField('Climbing')
    eating = models.BooleanField('Eating')
    foraging = models.BooleanField('Foraging')
    other_Activities = models.CharField('Other_Activities',max_length=50)
    kuks = models.BooleanField('Kuks')
    quaas = models.BooleanField('Quaas')
    moans = models.BooleanField('Moans')
    tail_flags = models.BooleanField('Tail_flags')
    tail_twitches = models.BooleanField('Tail_twitches')
    approaches = models.BooleanField('Approaches')
    indifferent = models.BooleanField('Indifferent')
    runs_from = models.BooleanField('Runs_from')
