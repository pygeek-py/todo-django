from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import item

class registerform(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    
    class Meta():
        model = User
        fields = ["username", "phone", "email", "password1", "password2"]
        
class itemform(forms.ModelForm):
    class Meta():
        model = item
        fields = '__all__'
        exclude = ["user"]