from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MyUserForm(UserCreationForm):
    forms.EmailField(required=True,label='Email')
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
    def save(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email=self.changed_date['email']
        if commit:
            user.save()
        
    
    