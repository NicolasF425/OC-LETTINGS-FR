from django.shortcuts import render
from lettings.models import Letting


# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
# Cras eget scelerisque
def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
