from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import island,eastern,western,predict,norms
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Create your views here.
def home(request):
    return render(request,'index.html')

def pred_population(datas,year):
        x=[]
        y=[]
        z=[[int(year)]]
        for data in datas:
            x.append([data.year.year])
            y.append([(data.actualDem)])
        x = np.array(x)
        y = np.array(y)
        poly = PolynomialFeatures(degree=2)
        x_poly = poly.fit_transform(x)
        lin = LinearRegression()
        lin.fit(x_poly,y)
        z = np.array(z)
        val=lin.predict(poly.fit_transform(z))
        print(round(val[0][0],2))
        return round(val[0][0],2)

def pred_demand(datas,year):
        x=[]
        y=[]
        z=[[int(year)]]
        for data in datas:
            x.append([data.year.year])
            y.append([(data.actualDem)])
        
        x = np.array(x)
        y = np.array(y)
        poly = PolynomialFeatures(degree=2)
        x_poly = poly.fit_transform(x)
        lin = LinearRegression()
        lin.fit(x_poly,y)
        z = np.array(z)
        val=lin.predict(poly.fit_transform(z))
        print(round(val[0][0],2))
        return round(val[0][0],2)

def prediction(request):
    if request.method == 'POST':
        year = request.POST['drop']
        westerns = western.objects.all()
        easterns = eastern.objects.all()
        islands = island.objects.all()
        # west_dem = pred_demand(westerns,year)
        # east_dem = pred_demand(easterns,year)
        # island_dem = pred_demand(islands,year)
        # west_popln = pred_population(westerns,year)
        # east_popln = pred_population(easterns,year)
        # island_popln = pred_population(islands,year)
        # dem_value = west_dem+east_dem+island_dem
        # popln_value = west_popln + east_popln + island_popln

        return render(request,'demand.html',{"values":value,"year":year})
    else :
        return redirect(home)