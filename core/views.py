from django.shortcuts import render
from .models import EmployeeModel

# Create your views here.


def home(request):
    emploees = EmployeeModel.objects.all()
    return render (request, 'core/home.html',{'emploees':emploees})
