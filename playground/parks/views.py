from django.shortcuts import render

def get_parks(request):
    return render(request, 'parks.html', {})