from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import ShortUrl

import base64
import unirest
import json

# handle shortened url requests
def index(request, url_hash):
    short_url = ShortUrl.objects.get(url_hash=url_hash)

    return redirect(short_url.original_url)


def generate(request):
    url = request.GET.get('url', '')

    # check cache
    if url not in cache:
        # service call to phishtank
        response = unirest.post(
            "http://checkurl.phishtank.com/checkurl/",
            params={
                "app_key": "df0bbae9d44d378c5c86df29628a41142d61ee8dd275808fe6e0b11972e62bf5",
                "url": base64.b64encode(url),
                "format": "json",
            },
        )

        # check if it's a phish site, if not, create short_url
        if not response.body["results"]["in_database"]:
            short_url = ShortUrl.objects.create_url(url)
            response.body['url_hash'] = short_url.url_hash
        else:
            response.body['url_hash'] = "PHISHING_SITE"

        # set cache
        cache.set(url, response)
        response.body['cached'] = False

    else:
        # url has already been checked
        response = cache.get(url)
        response.body['cached'] = True

    return HttpResponse(json.dumps(response.body), content_type="application/json")
