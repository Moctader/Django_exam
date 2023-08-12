from django.shortcuts import render, redirect
from first_app.forms import To_Do_form
from first_app.models import To_Do_Model

# Create your views here.
def home(request):
    return render(request, 'base.html')

def TaskModel(request):
    if request.method=="POST":
        book=To_Do_form(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save()
            return redirect('Show_tasks')
    else:
        book=To_Do_form()
    return render(request,'TaskModel.html', {'form':book})

def Show_tasks(request):
    book=To_Do_Model.objects.all()
    for item in book:
        print(item.taskTitle)
    return render(request, 'show_tasks.html', {'book':book})

def Edit_button(request, id):
    
    book=To_Do_Model.objects.get(pk=id)
    form=To_Do_form(instance=book) 
    if request.method=="POST":
        form=To_Do_form(request.POST, instance=book)   
        if form.is_valid():
            form.save()
            return redirect('Show_tasks')
    # else:
    return render(request, 'TaskModel.html', {'form':form})

def Delete_button(request, id):
    book=To_Do_Model.objects.get(pk=id).delete()
    return redirect('Show_tasks')

def Complete_button(request, id):
    book=To_Do_Model.objects.get(pk=id).delete()
    return render(request, 'complete_task.html', {'book':book})
