from django.shortcuts import render


def index(request):
    """A View to return to the index page"""

    return render(request, 'home/index.html')
