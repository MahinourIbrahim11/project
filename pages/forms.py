from django import forms
from .models import Form

class LoginForm(forms.ModelForm):
   class Meta:
       model = Form
       fields = '__all__'
       widgets = {
                 'password': forms.PasswordInput(),
       }
