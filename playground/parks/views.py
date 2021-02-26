import os
import tempfile
from django.shortcuts import render

def get_parks(request):

    file = tempfile.TemporaryFile(
        dir="/tmp/my_subdirectory", mode='"w+"
    )

    return render(request, 'parks.html', {})
