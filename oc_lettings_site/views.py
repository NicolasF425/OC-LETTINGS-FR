from django.shortcuts import render


def index(request):
    """
    View for the index page
    """
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """
    Custom view for the 404 error
    """
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Custom view for the 500 error
    """
    return render(request, '500.html', status=500)
