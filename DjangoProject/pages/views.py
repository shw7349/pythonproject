from django.shortcuts import render

def landing(request):
    return render(
        request,
        'pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'pages/about_me.html'
    )