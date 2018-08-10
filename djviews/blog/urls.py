from django.conf.urls import url

# from .views import list_views # Request this one view
from .views import (
    list_views,
    detail_view,
    create_view,
    update_view,
    delete_view,
    )

urlpatterns = [
    url(r'^$', list_views, name='list'),
    url(r'^create/$', create_view, name='create'),
    # url(r'^1/$', detail_view, name='detail'),
    url(r'^(?P<id>\d+)/$', detail_view, name='detail'), #url param get value 'id' 
    url(r'^(?P<id>\d+)/edit/$', update_view, name='update'), #url param get value 'id' 
    url(r'^(?P<id>\d+)/delete/$', delete_view, name='delete'), #url param get value 'id' 
]