from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse

def customer_add(request):
    return render(request,"customer/base.html")