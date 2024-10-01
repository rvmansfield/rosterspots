from django import forms
from .models import Teams
from django.utils.text import slugify



class TeamForm(forms.ModelForm):
    
    
    
    STATES = ( 
    ("NC", "NC"), 
    ("SC", "SC"), 
    ("VA", "VA"), 
    
) 
    
    

    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=False, widget=forms.Select(choices=STATES,attrs={'class': 'form-control'}))
    contactName = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
   



    class Meta:
        model = Teams
        fields = ['name','city','state','contactName']

