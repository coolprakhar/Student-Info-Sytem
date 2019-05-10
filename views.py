from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def home_page_view(request):
    #students=Student.objects.all()
    #students=Student.objects.filter(marks__lt=35) #marks less than 35
    #students=Student.objects.filter(name__startswith='A')
    #students=Student.objects.all().order_by('marks')
    students=Student.objects.all().order_by('-marks')

    #This is called Object Relational Model
    return render(request,'testapp/index.html',{'students':students})
