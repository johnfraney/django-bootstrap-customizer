# -*- coding: utf-8 -*-
from django.urls import path
from .views import CSSBelowTheFoldView


app_name = 'bootstrap_customizer'
urlpatterns = [
    path(
        'bootstrap_css_below_the_fold-<str:hash>.min.css',
        CSSBelowTheFoldView.as_view(),
        name='bootstrap_css_below_the_fold'
    ),
]
