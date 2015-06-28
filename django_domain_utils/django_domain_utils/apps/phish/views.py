from django.core.cache import cache
from django.http import HttpResponse
import base64
import unirest
import json


def index(request):
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

        # set cache
        cache.set(url, response)
        response.body['cached'] = False
    else:
        # url has already been checked
        response = cache.get(url)
        response.body['cached'] = True

    return HttpResponse(json.dumps(response.body), content_type="application/json")
