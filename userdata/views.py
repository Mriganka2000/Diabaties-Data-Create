from django.shortcuts import render
from .forms import UserDataForm


def userdata(request):
    form = UserDataForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'userdata/form.html', context)