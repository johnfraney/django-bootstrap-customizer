# Middleware

## `BootstrapThemeMiddleware`

`bootstrap_customizer.middleware.BootstrapThemeMiddleware`

Uses the current [`Site`](https://docs.djangoproject.com/en/dev/ref/contrib/sites/#django.contrib.sites.models.Site) and [`SiteBootstrapTheme`](models.md#sitebootstraptheme) to add the current site's [`BootstrapTheme`](models.md#bootstraptheme) to the request.

Attributes:

- `request.bootstrap_theme` - `BootstrapTheme` instance for the current site
