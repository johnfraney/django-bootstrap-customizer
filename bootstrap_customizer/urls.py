# -*- coding: utf-8 -*-
from .views import CSSBelowTheFoldView

app_name = 'bootstrap_customizer'

try:
    from django.urls import path


    urlpatterns = [
        path(
            'bootstrap_css_below_the_fold-<str:hash>.min.css',
            CSSBelowTheFoldView.as_view(),
            name='bootstrap_css_below_the_fold'
        ),
    ]

except:
    from django.conf.urls import url


    urlpatterns = [
        url(
            'bootstrap_css_below_the_fold-(?P<page_slug>[\w]+).min.css',
            CSSBelowTheFoldView.as_view(),
            name='bootstrap_css_below_the_fold'
        ),
    ]
