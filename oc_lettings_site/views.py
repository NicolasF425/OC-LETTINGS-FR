"""
oc_lettings_site/views.py
Index and custom views for errors 404 and 500
"""

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
    import sentry_sdk
    sentry_sdk.capture_message(f"Page not found: {request.path}", level="warning")
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Custom view for the 500 error
    """
    return render(request, '500.html', status=500)
