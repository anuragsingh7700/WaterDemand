from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import island,eastern,western,predict
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import locale

# Create your views here.
def home(request):
    return render(request,'index.html')

def pred_population(datas,year):
        x=[]
        y=[]
        z=[[int(year)]]
        for data in datas:
            x.append([data.year])
            y.append([data.population])
        x = np.array(x)
        y = np.array(y)
        # poly = PolynomialFeatures(degree=2)
        # x_poly = poly.fit_transform(x)
        # lin = LinearRegression()
        # lin.fit(x_poly,y)
        # z = np.array(z)
        # val=lin.predict(poly.fit_transform(z))

        lin = LinearRegression()
        lin.fit(x, y) 
        val = lin.predict(z)
        print(round(val[0][0],2))
        return round(val[0][0],2)

def pred_demand(datas,popln):
        x=[]
        y=[]
        z=[[int(popln)]]
        for data in datas:
            x.append([data.population])
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
        old_total_dem=[]
        total_population=[]
        # print(len(westerns))
        # i = 0
        for i in range(len(westerns)):
            old_total_dem.append((westerns[i].actualDem))
            old_total_dem[i] += easterns[i].actualDem
            old_total_dem[i] += islands[i].actualDem
            # old_west_popln.append()
            # total_population.append([westerns[i].year,westerns[i].population + easterns[i].population + islands[i].population]) 


        west_popln = pred_population(westerns,year)
        east_popln = pred_population(easterns,year)
        island_popln = pred_population(islands,year)
        total_population = west_popln + east_popln + island_popln

        west_dem = pred_demand(westerns,west_popln )
        east_dem = pred_demand(easterns,east_popln )
        island_dem = pred_demand(islands,island_popln )
        dem_value = west_dem + east_dem + island_dem
        
        locale.setlocale(locale.LC_ALL, 'en_US')
        # print(locale.format('%d',, grouping=True))   # returns '4,294,967,296'
        
        print(f"total population :{total_population}")
        print(f"total demand :{dem_value}")
        return render(request,'demand.html',
            {
                "old_total_dem":old_total_dem,
                "western":westerns,
                "eastern":easterns,
                "island":islands,
                "west_dem":west_dem,
                "east_dem":east_dem,
                "island_dem":island_dem,
                "popln_value":locale.format('%d',round(total_population,2), grouping=True),
                "dem_value":round(dem_value,2),
                "year":year
            })
    else :
        return redirect(home)


def reference(request):
    return render(request,'reference.html')