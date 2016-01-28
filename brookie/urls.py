from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^invoice/(?P<pk>[\d]+)/pdf/$',
        views.generate_invoice,
        name='generate-invoice'),

    url(r'^invoice/(?P<pk>[\d]+)/download/$',
        views.view_invoice,
        name='view-invoice'),

    url(r'^quote/(?P<pk>[-\d]+)/pdf/$',
        views.generate_quote,
        name='generate-quote'),

    url(r'^quote/(?P<pk>[-\d]+)/invoice/$',
        views.quote_to_invoice,
        name='quote-to-invoice'),
]
