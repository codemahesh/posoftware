from tkinter import Widget
from unicodedata import name
from django import forms
from .models import Customer, CustomerPo, CustomerPoItem, Dispatch, Uom, VendorPo 

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomerPoForm(forms.ModelForm):
    
    category = forms.CharField(widget =forms.TextInput(attrs= {'class':'form-control','readonly':'True'}))   # same as inside meta class > widgets > 'category'   
    
    class Meta:
        model = CustomerPo
        fields = ['customer_id','customer_po_number','date','customer_code','address','place','category']
        widgets = {
            'customer_id':forms.Select(attrs={'class':'form-select'}),
            'customer_po_number':forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
            'date': forms.DateInput(attrs={'class':'form-control','autocomplete': 'off',}),
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_code': forms.TextInput(attrs={'class':'form-control'}),
            # 'category': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'address': forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 5,'readonly':'True'}),
            'place': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
        }
        
        
    def __init__(self, *args, **kwargs):
        super(CustomerPoForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'placeholder':'yyyy-mm-dd'})
        # self.fields['customer_name']
        # self.fields['customer_po_number']
        # print("This is self.data ",self.data)
        
        # if 'customer_id' in self.data:
        #     try:
        #         customer_id = self.data.get('customer_id')
        #         self.fields['customer_id'].queryset = Customer.objects.filter(id=customer_id)
        #     except(ValueError, TypeError):
        #         pass
        
        
        
class CustomerPoItemForm(forms.ModelForm):
    class Meta:
        model = CustomerPoItem
        fields = '__all__'
        widgets = {
            'customer_po_id':forms.Select(attrs={'class':'form-select'}),
            #  'customer_po_number':forms.Select(attrs={'class':'form-select'}),
             'customer_item_code': forms.TextInput(attrs={'class':'form-control'}),
             'customer_item_description':forms.Textarea(attrs={'class':'form-control','cols': 10, 'rows': 3,}),
             'quantity':forms.NumberInput(attrs={'class':'form-control'}),
             'unit': forms.Select(attrs={'class':'form-select'}),     
             
        }
    def __init__(self, *args, **kwargs):
        super(CustomerPoItemForm, self).__init__(*args, **kwargs)
        # exclude= ['customer_po_number']

class DispatchForm(forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = '__all__'
        widgets = {
            "customer_po_number":forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
            'date': forms.DateInput(attrs={'class':'form-control','autocomplete': 'off',}),
            'invoice_number': forms.TextInput(attrs={'class':'form-control'}),
            "dispatch_mail_status":  forms.Select(attrs={'class':'form-select'}),
            'docket': forms.TextInput(attrs={'class':'form-control'}),
            'parcel': forms.Select(attrs={'class':'form-select'}),
            'dimension': forms.TextInput(attrs={'class':'form-control'}),
            "charged_weight":forms.NumberInput(attrs={'class':'form-control'}),
            'weight':forms.NumberInput(attrs={'class':'form-control'}),
            'unit': forms.Select(attrs={'class':'form-select'}),
            'sender': forms.Select(attrs={'class':'form-select'}),
            'curior_company': forms.Select(attrs={'class':'form-select'}),
            'delivery_status': forms.Select(attrs={'class':'form-select'}),
            'delivery_date' : forms.DateInput(attrs={'class':'form-control','autocomplete': 'off',}),
            "invoice_status" :forms.Select(attrs={'class':'form-select'}),
            'insurance' :forms.Select(attrs={'class':'form-select'}),
            'remark':  forms.TextInput(attrs={'class':'form-control'}),
            'asn_number': forms.TextInput(attrs={'class':'form-control'}),
        }

class VendorPoForm(forms.ModelForm):
    
    class Meta:
        model = VendorPo
        fields = ['customer_po_number','our_po_number','vendor_name','po_date']
        # exclude =('acknowledgement_date')
        widgets = {
           'customer_po_number':forms.TextInput(attrs={'class':'form-control'}),
           'our_po_number': forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
           'vendor_name': forms.TextInput(attrs={'class':'form-control'}),
           'po_date': forms.DateInput(attrs={'class':'form-control','autocomplete': 'off',}),
        }