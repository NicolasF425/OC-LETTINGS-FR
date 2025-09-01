from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


def index(request):
    """
    List view for lettings
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View for a letting
    """
    letting = get_object_or_404(Letting, pk=letting_id)

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
