
from django.db import models
#from djgeojson.fields import PointField
#from django.contrib.gis.db import models as gismodels

# Create your models here.asdsdf

#class CountyDat(models.Model):
#    name=models.CharField(max_length=500)
#    AvgAgeYounger=models.FloatField(max_length=5)
#    AvgBRChange=models.FloatField(max_length=5)
#    MoreInfo=models.URLField(max_length=1000, default='')

#    geom=gismodels.PointField()
#    objects=gismodels.GeoManager()
#    def __unicode__(self):
#        return self.name

class submit(models.Model):
    comment=models.CharField(max_length=500)
    name=models.CharField(max_length=250)
    date=models.DateField()


    def __str__(self):
        return str(self.name) + " : " + str(self.date) + " : " + str(self.comment)
class fact(models.Model):
    description=models.CharField(max_length=500)
    title=models.CharField(max_length=250)
    url=models.URLField(max_length=1000, default='')


    def __str__(self):
        return str(self.title) + " : " + str(self.url) + " : " + str(self.description)

class aboutl(models.Model):
    position=models.CharField(max_length=500)
    person_name=models.CharField(max_length=250)
    email=models.URLField(max_length=1000, default='')
    phone=models.IntegerField()


    def __str__(self):
        return str(self.person_name) + " : " + str(self.email) + " : " + str(self.position) + " : " + str(self.phone)
