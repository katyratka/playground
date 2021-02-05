from django.shortcuts import render
from django.http import HttpResponseRedirect


def get_playgrounds(request):
    url = request.GET.get("next", "/")
    return HttpResponseRedirect(url)
