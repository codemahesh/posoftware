from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Create your views here.
def  login_view(request):
    # if request.user.is_authenticated:
    #     return render(request,'accounts/already-logged-in.html',{})
    if request.method == 'POST':
         username =request.POST.get('username') 
         password = request.POST.get('password')
         print(username, password)
         user = authenticate(request, username=username, password= password)
         if user is None:
            context = {'error':"Invalid uername or password"}
            return render(request,'accounts/login.html',context)
         print(user)
         login(request, user)
         return redirect('showcustomerpo')
             
    return render(request,'accounts/login.html',{})
 
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html',{})
