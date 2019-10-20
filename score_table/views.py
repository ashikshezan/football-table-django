from django.shortcuts import render
from .script import competitions


def HomeView(request):
    table = competitions()
    # table_dict = {k: v for (k, v) in table}
    return render(request, 'home.html', {'table': table})
