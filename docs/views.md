# Views

## `CSSBelowTheFoldView`

`bootstrap_customizer.views.CSSBelowTheFoldView`

This view returns a CSS response containing the contents of the current site's `BootstrapTheme.css_below_the_fold`.

The view has a required `hash` keyword argument to uniquely identify it per-theme, obtained using `BootstrapTheme.get_hash()`. This allows the view to bust its cache when requesting the below-the-fold CSS for a different site, for instance.

The view is cached for `CACHE_MIDDLEWARE_SECONDS` seconds.

This view is most often referenced using the [`bootstrap_theme_css_below_the_fold_url` template tag](template_tags.md#bootstrap_theme_css_below_the_fold_url)
