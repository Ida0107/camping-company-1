from django.conf.urls import url
from customer.views import (user_page, book,
                            user_detail_page,
                            custom_itinerary)

app_name = "customer"

urlpatterns = [
    # url(r'^$', destination, name="welcome"),
    url(r'^$', user_page, name="user_page"),
    url(r'^(?P<pk>\d+)/detail/$', user_detail_page, name="user_detail_page"),
    url(r'^book/(?P<pk>\d+)/create/$', book, name="book"),
    url(r'^itinerary/$', custom_itinerary, name="custom_itinerary"),
]
