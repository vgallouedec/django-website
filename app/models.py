from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    inhabitants = models.IntegerField(default=0)



