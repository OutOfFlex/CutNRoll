from django.shortcuts import render


def home(request):
    return render(request, 'testapp\home.html')

def services(request):
    return render(request, 'testapp\services.html')

def contacts(request):
    return render(request, 'testapp\contacts.html')

def goods(request):
    return render(request, 'testapp\goods.html')

def staff(request):
    return render(request, 'testapp\staff.html')

def cabinet(request):
    return render(request, 'testapp\cabinet.html')
