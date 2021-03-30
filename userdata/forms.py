from django import forms
from .models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('peeatnight', 'peelevel', 'thirstylevel', 'feeltired', 'blurryvision', 'healing', 'hungrylevel', 'skin')