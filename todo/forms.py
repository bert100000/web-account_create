from django.forms import ModelForm
from .models import Todo 

class TodoForm(ModelForm):
    #設定
    class Meta:
        model=Todo
        # fields='__all__'
        fields=['title','text','important','completed']
        
        
    