from django import db
from django.shortcuts import render
from django.db.models.expressions import RawSQL


def get_parks(request):
    name = request.GET.get("name")
    raw = f'SELECT * FROM playground_parks WHERE name = {name}'

    # Option 1 for bad SQL injection
    cursor = db.cursor()
    cursor.execute(raw)

    # Option 2 for bad SQL injection
    test = RawSQL(raw)

    return render(request, 'parks.html', {})