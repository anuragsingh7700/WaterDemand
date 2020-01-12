from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import island,eastern,western,predict,norms
import numpy as np

# Create your views here.
def home(request):
    return render(request,'index.html')

def prediction(request):
    if request.method == 'POST':
        year = request.POST['drop']
        datas = western.objects.all()

        # x=[]
        # y=[]
        # count = 0

        # for data in datas:
        #     x.append([data.year.year])
        #     y.append([data.actualDem])
        #     count+=1

        # x=np.array(x)

        # for i in range (1,15):
        #     current_year = x[count-1]+i
        # current_year = int(current_year[0])+4
        # # return render(request,'demand.html',{"values":val})
        return render(request,'demand.html',{"values":current_year})
    else :
         return redirect(home)