from django.shortcuts import render

def get_playgrounds(request):
    return render(request, 'playgrounds.html', {})