from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from. models import Log
from .forms import LogForm

@login_required
def log_create_view(request):
    # Display form for user
    form = LogForm(request.POST or None)
    if form.is_valid():
        # save data for the current user
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/logs')

    context = {
        'form': form
    }
    return render(request, 'logs/create.html', context)

@login_required
def entry_view(request):
    current_user = request.user
    # gets list of objects for the current user
    entry_list = Log.objects.filter(user=current_user) 

    context = {
        'entry_list': entry_list
    }
    return render(request, 'logs/entries.html', context)

@login_required
def update_view(request, id):
    # gets Log objects by id but only for current user
    instance = get_object_or_404(Log, id=id, user=request.user)
    # Displays form to be updated and also shows previously entered data in the form fields
    form = LogForm(initial={'item': instance.item, 'cost': instance.cost},
    instance=instance)
    if request.method == 'POST':
        form = LogForm(request.POST, instance=instance)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/logs')
    
    context = {
        'form': form,
        'instance': instance
    }
    return render(request, 'logs/update.html', context)

@ login_required
def delete_view(request, id):
    # gets object by id for current user and deletes
    instance = get_object_or_404(Log, id=id, user=request.user)
    if request.method == "POST":
        instance.delete()
        return redirect('/logs')
    context = {
        "instance": instance
    }
    return render(request, "logs/delete.html", context)

def log_out_view(request):
    return render(request, 'logs/logout.html')









    
