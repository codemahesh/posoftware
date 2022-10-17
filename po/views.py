from cgi import print_environ
from cmath import log
import json
from logging.config import IDENTIFIER
from wsgiref.handlers import format_date_time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from po.forms import CustomerForm, CustomerPoForm, CustomerPoItemForm, DispatchForm, VendorPoForm
from po.models import Customer, CustomerPo, CustomerPoItem, VendorPo
from django.forms.models import modelformset_factory

#-------------------------Search-----------------------------------
def customerpo_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        print('searched  ==',searched)
        customerpo = CustomerPo.objects.filter(customer_po_number=searched)
        # customerPoItem = CustomerPoItem.objects.filter(customer_po_number= searched)
        # print("Context_dictionary",customerpo)
        # print('Custome po items ',customerPoItem)
        vendorpo = VendorPoForm()
        context = {
            'customerpo':customerpo.values,
            'vendorpo':vendorpo,
            # 'customerpoitem':customerPoItem
        }
        return render(request,'customerpo/searchCustomerPo.html', context=context)
    else:   
  
        return render(request,'customerpo/searchCustomerPo.html', context={})

#-------------------------Dashboard----------------------------------
def dashboard_show(request):
    return render(request,"dashboard.html")

#------------------------Customer details-------------------------------
@login_required
def customer_show(request):
    return render(request,"customer/customer_show.html")

@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showcustomer')
    else:
        form = CustomerForm()
    return render(request,'customer/customer_add.html',{'form':form})

@login_required
def customer_show(request):        
    context = {'customer':Customer.objects.all()}
    return render(request,'customer/customer_show.html',context)

@login_required  
def customer_update(request,id):
    customer_id = Customer.objects.get(pk=id)
    form = CustomerForm(request.POST or None, instance = customer_id)
    if form.is_valid():
        form.save()
        return redirect('showcustomer') 
    return render(request, 'customer/customer_update.html', {'form': form})
    
@login_required
def customer_delete(request,id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return redirect('showcustomer')

#-----------------------------Customer po methods-----------------------------
@login_required
def customerpo_show(request):
    print("hello")
    context = {'customerpo': CustomerPo.objects.all()}
    return render(request,'customerpo/customerpo_show.html',context)

@login_required
def customerpo_add(request):
    if request.method == 'POST':
        form = CustomerPoForm(request.POST)
        print("request.post::::",request.POST)
        print('tags in form is',form)
        if form.is_valid():
            # customerid = Customer.objects.filter(id=request.POST['customer_name'][0])           
            # customer_name = customerid.values('customer_name')[0]['customer_name']
            customer_id = form.cleaned_data['customer_id']
            print("This is customer id",customer_id)
            customer_name = Customer.objects.values_list('customer_name').get(id=customer_id)[0]
            customer_po = form.cleaned_data['customer_po_number']
            date = form.cleaned_data['date']
            customer_code = form.cleaned_data['customer_code']
            category = form.cleaned_data['category']
            address = form.cleaned_data['address']
            place = form.cleaned_data['place']
            
            reg =CustomerPo(customer_id = customer_id,customer_name=customer_name,customer_po_number=customer_po, date=date, customer_code =customer_code, category=category, address= address, place=place)
            reg.save()
        return redirect('showcustomerpo')
    else:
        form = CustomerPoForm()
    return render(request,'customerpo/customerpo_add.html',{'form':form})

@login_required   
def get_customer_code(request):
    data = json.loads(request.body)
    customer_code = data["id"]
    customer = Customer.objects.filter(customer_code=customer_code).order_by('customer_name')
    print("This is customer code",customer)
    return JsonResponse(list(customer.values('id','customer_name','category','address','place')), safe=False)

@login_required
def get_customer_detail(request):
    data = json.loads(request.body)
    customer_id = data["id"]
    customer = Customer.objects.filter(id=customer_id)
    print("This is customer id",customer)
    return JsonResponse(list(customer.values('category','address','place')), safe=False)


@login_required
def get_customerpo_table_id(request):
    print("hello everyone")
    data =json.loads(request.body)
    customer_po_number = data['id']
    customerpo = CustomerPo.objects.filter(customer_po_number=customer_po_number)
    print("This is customer id  1",customerpo)
    print('This is real id',customerpo.values('id'))
    return JsonResponse(list(customerpo.values('id')), safe=False)


@login_required
def customerpo_update(request,id=None):
    
    obj = get_object_or_404(CustomerPo, id=id)
    print("This is obj",obj)
    form = CustomerPoForm(request.POST or None, instance = obj)
    print()
    CustomerPoItemFormset = modelformset_factory(CustomerPoItem, form = CustomerPoItemForm, extra = 0)
    # customerpono = CustomerPo.objects.filter(id=id).values()
    # print("this is customerpono", customerpono[0]["customer_name"])
    # customername =customerpono[0]["customer_name"]
    qs = obj.customerpoitem_set.all()
    formset = CustomerPoItemFormset(request.POST or None, queryset=qs)
    print("formset :",formset)
    context ={
        'form':form,
        'formset': formset,
        'object':obj,

    }
    if request.method == 'POST':
        if all([form.is_valid(), formset.is_valid()]):
            print("Thi is form",form)
            parent = form.save(commit=False)
            customer_id = form.cleaned_data['customer_id']
            customer_name = Customer.objects.values_list('customer_name').get(id=customer_id)[0]
            parent.customer_name = customer_name
            print("parent.customer_id issss ", parent.customer_id)
            print("parent.customer_name issss ", parent.customer_name)
            print("parent ::",parent)
            parent.save()
            for form in formset:
                child = form.save(commit = False)
                child.customerpo = parent
                child.save()
            context['message'] = 'Data saved.'
            return redirect('showcustomerpo')
        
    return render(request, 'customerpo/customerpo_update.html', context)
    


@login_required
def customerpo_delete(request,id):
    if request.method == 'POST':
        customerpo = CustomerPo.objects.get(pk=id)
        customerpo.delete()
        return redirect('showcustomerpo')
    
    
@login_required
def customerpoitem_delete(request, id):
    print("This is delete test")
    if request.method == 'POST':
        customerpoitem = CustomerPoItem.objects.get(pk=id)
        customerpoitem.delete()
        return redirect('showcustomerpo')
    

#--------------------Supplier View------------------------------
@login_required
def add_vendor_deatil(request):
    if request.method == 'POST':
        form = VendorPoForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('showcustomerpo')
    
  
  
    
    
#---------------------dispatch view------------------------------
@login_required
def add_dispatch(request):
    if request.method == 'POST':
        form = DispatchForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dispatch')
    else:
        form = DispatchForm()
        print("VALUR of  form", form)
    return render(request,'dispatch/dispatch.html',{'form':form})
    
    
