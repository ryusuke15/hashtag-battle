from django.conf.urls import url
from .views import single_battle

urlpatterns = [
    url(r'^api/(?P<id>[0-9]+)/$', single_battle,  name='detail')
]
