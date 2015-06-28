from django.core.cache import cache
from django.http import HttpResponse
import json
import socket


def index(request):

    valid = False
    cached = False
    ip = ""

    domain_name = request.GET.get('domain', '')

    if not domain_name == '':
        # check cache for existing entry
        if domain_name not in cache:
            # attempt ip lookup, fail gracefully if a problem arises
            try:
                ip = socket.gethostbyname(domain_name)
                valid = True
                # cache response
            except socket.gaierror:
                # ip doesn't exist for domain
                ip = ""
                valid = False

            # cache values
            cache.set(domain_name, {'valid': valid, 'ip': ip})

        else:
            # return cached results
            valid = cache.get(domain_name)['valid']
            ip = cache.get(domain_name)['ip']
            cached = True

    def default(obj):
        # handle json encoding of date objects
        import datetime

        if isinstance(obj, datetime.datetime):
            if obj.utcoffset() is not None:
                obj = obj - obj.utcoffset()
        millis = int(obj.strftime("%s"))
        return millis

    return HttpResponse(json.dumps({'cached': cached, 'valid': valid, 'ip': ip}, default=default),
                        content_type="application/json")
