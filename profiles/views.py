"""views definitions for profiles"""
import logging

from django.core.cache import cache
from django.shortcuts import get_object_or_404, render

from .models import Profile

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
#  sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """index view

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("profiles-DEBUG")
    logger.info("profiles-INFO")
    logger.warning("profiles-WARNING")
    logger.error("profiles-ERROR")
    logger.critical("profiles-CRITICAL")
    # ---------------------------------------
    profiles_list = cache.get("all_profiles")
    if profiles_list:
        logger.info("set the profiles cache")
    else:
        logger.info("set the profiles cache")
        profiles_list = Profile.objects.all()
        cache.set("all_profiles", profiles_list)

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
#  Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et
#  netus et males
def profile(request, username):
    """profile view for a username

    Args:
        request (_type_): _description_
        username (str): username

    Returns:
        _type_: _description_
    """
    a_profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": a_profile}
    return render(request, "profiles/profile.html", context)
