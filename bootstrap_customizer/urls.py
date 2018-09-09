# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import CSSBelowTheFoldView


app_name = 'bootstrap_customizer'
urlpatterns = [
    url('bootstrap_css_below_the_fold.min.css', CSSBelowTheFoldView.as_view(), name='bootstrap_css_below_the_fold'),
]
