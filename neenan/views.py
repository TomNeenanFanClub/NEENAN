from django.shortcuts import render

def home(request):
    return render(request, 'neenan/home.html')
