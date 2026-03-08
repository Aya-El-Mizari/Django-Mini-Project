from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'Home',
        'welcome_message': 'Welcome to my Django MiniSite!',
        'description': 'This is my mini Django project for Week 4.'
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'page_title': 'About',
        'name': 'Aya El Mizari',
        'bio': 'I am learning Django web development.',
        'skills': ['Python', 'HTML', 'CSS', 'Django']
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
        'page_title': 'Contact',
        'email': 'aya.elmizari@gmail.com',
        'phone': '+123 456 7890',
        'social_media': {
            'github': 'https://github.com/Aya-El-Mizari',
            'linkedin': 'https://www.linkedin.com/in/aya-el-mizari-035250384/'
        }
    }
    return render(request, 'core/contact.html', context)