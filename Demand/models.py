from django.db import models
from django.db.models import signals
from django.dispatch import receiver
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
# Create your models here.
class norms(models.Model):
    year = models.IntegerField(primary_key=True)
    low = models.IntegerField()
    high = models.IntegerField()

class island(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    population = models.IntegerField()
    # high = models.IntegerField()
    # normsPred = models.IntegerField()
    actualDem = models.IntegerField()

class eastern(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    population = models.IntegerField()
    # high = models.IntegerField()
    # normsPred = models.IntegerField()
    actualDem = models.IntegerField()
    
class western(models.Model):
    year = models.ForeignKey(norms,on_delete=models.CASCADE)
    population = models.IntegerField()
    # high = models.IntegerField()
    # normsPred = models.IntegerField()
    actualDem = models.IntegerField()    

class predict(models.Model):
    year = models.IntegerField(unique=True)
    island = models.IntegerField()
    western = models.IntegerField()
    eastern = models.IntegerField()
    total = models.IntegerField()




def prediction(object):
    #linear regression working code
        datas = western.objects.all()

        x=[]
        y=[]
        z = []
        # z = np.array(z)
        # for data in datas:
        #     x.append([data.year.year])
        #     y.append([data.actualDem])
        # # x = np.array(x)
        # # y = np.array(y)
        # lin = LinearRegression()
        # lin.fit(x, y) 
        # val = lin.predict(x)
        # rmse = np.sqrt(mean_squared_error(y,val))
        # r2 = r2_score(y,val)

        #Polynomial regression working code

        for data in datas:
            x.append([data.year.year])
            y.append([data.actualDem])
            count+=1


        
        x = np.array(x)
        y = np.array(y)
        poly = PolynomialFeatures()
        x_poly = poly.fit_transform(z)
        lin = LinearRegression()
        lin.fit(x_poly,y)
        val=lin.predict(poly.fit_transform(y))
        # rmse = np.sqrt(mean_squared_error(y,val))
        # r2 = r2_score(y,val)



#Signals Implementation for calculating prediction values
@receiver(signals.post_save,sender=western)
def calcwest(sender,instance,**kwargs):
    prediction(sender)

@receiver(signals.post_save,sender=eastern)
def calceast(sender,instance,**kwargs):
    prediction(sender)

@receiver(signals.post_save,sender=island)
def calcisland(sender,instance,**kwargs):
    prediction(sender)