from tkinter import Widget
from django import forms
from .models import Customer, CustomerPo, Uom 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
            'customer_code': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'address': forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 5}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
        
        }


class CustomerPoForm(forms.ModelForm):
    
    class Meta:
        model = CustomerPo
        fields = '__all__'
        widgets = {
            'customer_po_number': forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
            'date': forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd','autocomplete': 'off',}),
            'customer_name': forms.Select(attrs={'class':'form-select'}),
            'customer_code': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'address': forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 5,'readonly':'True'}),
            'place': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
        }
