from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import island,eastern,western,predict
# Create your views here.
def home(request):
    return render(request,'index.html')

def prediction(request):
    if request.method == 'POST':
        year = request.POST['drop'] 
        total = {
            "year" : year,
            "area" : "Mumbai"
        }
        return render(request,'demand.html',total)
    else :
         return redirect(home)
