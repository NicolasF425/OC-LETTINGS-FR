"""
profiles/views.py
Views file for the profile app
"""

from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
import logging
import sentry_sdk


logger = logging.getLogger(__name__)


def index(request):
    """
    List view for profiles
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error("Erreurwith profiles", exc_info=True)
        sentry_sdk.capture_exception(e)  # send error to Sentry
        raise  # send error 500


def profile(request, username):
    """
    View for a profile
    """
    logger.debug(f"Access to detail for profile {username}")

    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(f"Erreur with profil {username}", exc_info=True)
        sentry_sdk.capture_exception(e)
        raise
