from django.utils.deprecation import MiddlewareMixin

from bootstrap_customizer.models import BootstrapTheme


class BootstrapThemeMiddleware(MiddlewareMixin):
    """
    Middleware that sets `bootstrap_theme_updated` attribute to request object.
    """

    def process_request(self, request):
        theme = BootstrapTheme.objects.filter(sitebootstraptheme__site=request.site).first()
        if theme:
            request.bootstrap_theme = theme
