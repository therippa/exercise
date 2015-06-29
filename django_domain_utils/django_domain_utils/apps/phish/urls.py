from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^generate/$', views.generate, name='generate'),
    url(r'^(?P<url_hash>\w+)/$', views.index, name='index'),
]