from django import forms 
from . import models 

class CreateCommunity(forms.ModelForm): 
    class Meta: 
        model = models.community
        fields = ['name','description','slug','avatar']