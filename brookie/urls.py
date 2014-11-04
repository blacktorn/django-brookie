from django.conf.urls import *

urlpatterns = patterns(
    'brookie.views',
    url(r'^invoice/(?P<pk>[\d]+)/pdf/$',
        'generate_invoice',
        name='generate-invoice'),

    url(r'^invoice/(?P<pk>[\d]+)/download/$',
        'view_invoice',
        name='view-invoice'),

    url(r'^quote/(?P<pk>[-\d]+)/pdf/$',
        'generate_quote',
        name='generate-quote'),

    url(r'^quote/(?P<pk>[-\d]+)/invoice/$',
        'quote_to_invoice',
        name='quote-to-invoice'),
)
