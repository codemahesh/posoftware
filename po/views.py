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
            form.save()
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
    pass

def customerpo_delete(request,id):
    pass