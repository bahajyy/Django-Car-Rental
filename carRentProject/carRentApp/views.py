from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from django.contrib import messages
from django.http import HttpResponse
from .models import Car, Client

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)         
            Client.objects.create(user=user, country=form.cleaned_data['country'], city=form.cleaned_data['city'])
            messages.success(request, 'Başarıyla kayıt oldunuz!')
            return redirect('home')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password']

        # Authenticate using the email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            
            # Giriş yaptıktan sonra anasayfaya yönlendir ve hoşgeldin mesajı göster
            messages.success(request, f'Hoşgeldin, {user.username}!')
            
            return redirect('home')  
        else:
            messages.error(request, 'Giriş başarısız. Lütfen bilgilerinizi kontrol edin.')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def search_results(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        city = request.GET.get('city')
        brand = request.GET.get('brand')
        price_sort = request.GET.get('price_sort')
        transmission = request.GET.get('transmission')

        # Filtre ve sıralama işlemleri
        cars = Car.get_available_cars(start_date, end_date, city)

        if brand:
            cars = cars.filter(brand=brand)
        if transmission:
            cars = cars.filter(transmission=transmission)

        if price_sort == 'asc':
            cars = cars.order_by('cost_of_rental')
        elif price_sort == 'desc':
            cars = cars.order_by('-cost_of_rental')

        return render(request, 'searchResults.html', {'cars': cars})

    return HttpResponse("Invalid Request")
