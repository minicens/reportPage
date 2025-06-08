from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def abort(request):
    return render(request, 'abort.html')

def intro(request):
    return render(request, 'intro.html')

def service(request):
    return render(request, 'service.html')

