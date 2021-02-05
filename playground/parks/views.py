import os
from django.shortcuts import render

def get_parks(request):

    tmp_dir = os.environ.get('TMPDIR')
    file = open(tmp_dir+"/tmp","w+")

    return render(request, 'parks.html', {})
