"""
lettings/views.py
Views file for the lettings app
"""

import logging
import sentry_sdk
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting


logger = logging.getLogger(__name__)


def index(request):
    """
    List view for lettings
    """
    logger.info("Access to lettings page")

    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error("Erreur with lettings", exc_info=True)
        sentry_sdk.capture_exception(e)  # send error to Sentry
        raise  # send error 500


def letting(request, letting_id):
    """
    View for a letting
    """
    logger.debug(f"Access to detail for letting ID={letting_id}")

    try:
        letting = get_object_or_404(Letting, pk=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(f"Erreur with letting ID={letting_id}", exc_info=True)
        sentry_sdk.capture_exception(e)
        raise
