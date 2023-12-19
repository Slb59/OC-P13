import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam
# lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget
#  feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat
#  ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque
#  iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    logger.debug("main-DEBUG")
    logger.info("main-INFO")
    logger.warning("main-WARNING")
    logger.error("main-ERROR")
    logger.critical("main-CRITICAL")
    return render(request, "index.html")


def page_not_found(request, exception):
    response = render(request, "base/404.html", {})
    response.status_code = 404
    return response


def server_error(request, exception=None):
    response = render(request, "base/500.html", {})
    response.status_code = 500
    return response


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
        return division_by_zero
    except ZeroDivisionError:
        raise ZeroDivisionError
