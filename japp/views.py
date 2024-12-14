from django.shortcuts import render,redirect
from .forms import studentform
from .models import student
# Create your views here.
def studentview(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=studentform()
    return render(request, 'student.html', {'form':form})

def student_list(request):
    users=student.objects.all()
    return render(request,'student_list.html', {'users':users})
    

