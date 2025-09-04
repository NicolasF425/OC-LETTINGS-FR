from django.shortcuts import render


# olutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')
