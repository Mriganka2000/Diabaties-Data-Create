from django.shortcuts import render
from .forms import UserDataForm
from userdata.models import OriginalData


def userdata(request):
    form = UserDataForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            pregnency = form.cleaned_data['noofpregnency']
            # print(height, weight)
            height = height/100
            bmi = round(weight/(height*height), 1)
            # print(bmi)
            calculatedData = OriginalData(pregnency=pregnency, bmi=bmi)
            calculatedData.save()
            form.save()
    context = {
        'form': form
    }
    return render(request, 'userdata/form.html', context)