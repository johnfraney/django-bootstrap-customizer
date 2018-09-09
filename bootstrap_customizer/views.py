from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views.generic import View

from .models import SiteBootstrapTheme


class CSSBelowTheFoldView(View):
    def get(self, request):
        site_theme = SiteBootstrapTheme.objects.select_related('bootstrap_theme').get(
            site_id=get_current_site(request)
        )
        css_below_the_fold = site_theme.bootstrap_theme.css_below_the_fold
        return HttpResponse(css_below_the_fold, content_type='text/css')
