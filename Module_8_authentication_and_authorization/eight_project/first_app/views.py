from django.shortcuts import render
from first_app.forms import userResigstrationFrom

# Create your views here.
def home(request):
    if request.method=='POST':
        form=userResigstrationFrom(request.POST)
        if form.is_valid():
            form.save(commit=False)
            print(form.cleaned_data)
    else:
        form=userResigstrationFrom()         
    return render(request, 'base.html', {'form':form})