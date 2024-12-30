from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Consume
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'myApp/login.html')



@login_required
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            food_consumed = request.POST['food_consumed']
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume)
            consume.save()
            foods = Food.objects.all()
        else:
            foods = Food.objects.all()

        consumed_food = Consume.objects.filter(user=request.user)
    else:
        return redirect('login')
    
    context = {'foods': foods, 'consumed_food': consumed_food}
    return render(request, 'myApp/home.html', context) 

def delete_consume(request, pk):
    consumed_food = Consume.objects.get(id=pk)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myApp/delete.html')
    
              