from django.shortcuts import render


def signup(request):
    return render(request, 'accounts/signup.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # TODO Nee to logout and route to home page
    return render(request, 'accounts/signup.html')
