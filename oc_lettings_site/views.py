from django.shortcuts import render


# olutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
