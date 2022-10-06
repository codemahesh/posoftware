import json
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from po.forms import CustomerForm, CustomerPoForm
from po.models import Customer, CustomerPo

#------------------------Customer details-------------------------------
def customer_show(request):
    return render(request,"customer/customer_show.html")

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('showcustomer')
    else:
        form = CustomerForm()
    return render(request,'customer/customer_add.html',{'form':form})

def customer_show(request):
    context = {'customer':Customer.objects.all()}
    return render(request,'customer/customer_show.html',context)
    
def customer_update(request,id):
    customer_id = Customer.objects.get(pk=id)
    form = CustomerForm(request.POST or None, instance = customer_id)
    if form.is_valid():
        form.save()
        return redirect('showcustomer') 
    return render(request, 'customer/customer_update.html', {'form': form})
    

def customer_delete(request,id):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=id)
        customer.delete()
        return redirect('showcustomer')

#-----------------------------Customer po methods-----------------------------
def customerpo_show(request):
    print("hello")
    context = {'customerpo': CustomerPo.objects.all()}
    return render(request,'customerpo/customerpo_show.html',context)

def customerpo_add(request):
    if request.method == 'POST':
        form = CustomerPoForm(request.POST)
        print("form",form)
        if form.is_valid():
            customerid = Customer.objects.filter(id=request.POST['customer_name'][0])
            
            customer_name = customerid.values('customer_name')[0]['customer_name']
            customer_po = form.cleaned_data['customer_po_number']
            date = form.cleaned_data['date']
            customer_code = form.cleaned_data['customer_code']
            category = form.cleaned_data['category']
            address = form.cleaned_data['address']
            place = form.cleaned_data['place']
            
            reg =CustomerPo(customer_name=customer_name,customer_po_number=customer_po, date=date, customer_code =customer_code, category=category, address= address, place=place)
            reg.save()
        return redirect('showcustomerpo')
    else:
        form = CustomerPoForm()
    return render(request,'customerpo/customerpo_add.html',{'form':form})
    
def get_customer_code(request):
    data = json.loads(request.body)
    customer_code = data["id"]
    customer = Customer.objects.filter(customer_code=customer_code).order_by('customer_name')
    print("This is customer code",customer)
    return JsonResponse(list(customer.values('id','customer_name','category','address','place')), safe=False)

def get_customer_detail(request):
    data = json.loads(request.body)
    customer_id = data["id"]
    customer = Customer.objects.filter(id=customer_id)
    print("This is customer id",customer)
    return JsonResponse(list(customer.values('category','address','place')), safe=False)


def customerpo_update(request,id):
    customer_po = CustomerPo.objects.get(pk=id)
    form = CustomerPoForm(request.POST or None, instance = customer_po)
    if form.is_valid():
        customerid = Customer.objects.filter(id=request.POST['customer_name'][0])
        customer_po.customer_name = customerid.values('customer_name')[0]['customer_name']
        customer_po.customer_po_number = form.cleaned_data['customer_po_number']
        customer_po.date = form.cleaned_data['date']
        customer_po.customer_code = form.cleaned_data['customer_code']
        customer_po.category = form.cleaned_data['category']
        customer_po.address = form.cleaned_data['address']
        customer_po.place = form.cleaned_data['place']
        customer_po.save()
        return redirect('showcustomerpo') 
    return render(request, 'customerpo/customerpo_update.html', {'form': form})

def customerpo_delete(request,id):
    if request.method == 'POST':
        customerpo = CustomerPo.objects.get(pk=id)
        customerpo.delete()
        return redirect('showcustomerpo')