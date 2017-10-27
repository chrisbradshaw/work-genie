from django.conf.urls import url
from fitmarketapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
]
