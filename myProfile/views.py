from django.shortcuts import render

def home(request):

    context = {
        'navbarTab': 'home'
    }
    return render(request, 'profile/index.html', context)
