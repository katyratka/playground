from django.shortcuts import render

def get_parks(request):
    from parks.models import Park
    name = request.GET.get("name")
    # raw = Park.objects.raw(f'SELECT * FROM playground_parks WHERE name = {name}')

    Park.objects.get_or_create(
        name=name,
        description=name
    )
    return render(request, 'parks.html', {})