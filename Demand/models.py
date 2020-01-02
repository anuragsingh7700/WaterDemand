from django.db import models
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.
class norms(models.Model):
    year = models.IntegerField(primary_key=True)
    low = models.IntegerField()
    high = models.IntegerField()

class island(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    low = models.IntegerField()
    high = models.IntegerField()
    normsPred = models.IntegerField()
    actualDem = models.IntegerField()
        

class eastern(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    low = models.IntegerField()
    high = models.IntegerField()
    normsPred = models.IntegerField()
    actualDem = models.IntegerField()
    
class western(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    low = models.IntegerField()
    high = models.IntegerField()
    normsPred = models.IntegerField()
    actualDem = models.IntegerField()    

class predict(models.Model):
    year = models.IntegerField(unique=True)
    island = models.IntegerField()
    western = models.IntegerField()
    eastern = models.IntegerField()
    total = models.IntegerField()

@receiver(signals.post_save,sender=western)
def calcwest(sender,instance,**kwargs):
    return (sender)

@receiver(signals.post_save,sender=eastern)
def calceast(sender,instance,**kwargs):
    return (sender)

@receiver(signals.post_save,sender=island)
def calcisland(sender,instance,**kwargs):
    return (sender)