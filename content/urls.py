from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'events/$', views.events, name='events'),
    url(r'events/eventp/$', views.eventp, name='eventp'),
    url(r'events/eventw/$', views.eventw, name='eventw'),
    url(r'sponsors/$', views.sponsors, name='sponsors'),
    url(r'con16/$', views.con16, name='con16'),
]