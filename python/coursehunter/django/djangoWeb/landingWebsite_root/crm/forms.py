from tkinter import Button
from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone= forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class':'form-control'}) )
    # button=Button({"class":"class_input"})