from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    message_sent = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя: {name}, Email: {email}, Сообщение: {message}")
        message_sent = True
    return render(request, 'catalog/contacts.html', {'message_sent': message_sent})
