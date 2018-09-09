# Models

## `BootstrapTheme`

`bootstrap_customizer.models.BootstrapTheme`

This model stores Bootstrap variables and populates two fields with CSS chunks on `save()`: `css_above_the_fold` and `css_below_the_fold`.

**Note**: This model intentionally does not contain a field for every Bootstrap SCSS variable. It is meant to handle important Bootstrap SCSS variables to create a unique look & feel without overwhelming admins with choice.


### Bootstrap Fields

These fields correspond with [Bootstrap SCSS variables](https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss). Whereas Django uses `snake_case` for variables, Bootstrap's SCSS variables use `$kebab-case`. (Should we call that expensive kebab case?).

The `enable_rounded` field, for example, corresponds with the Bootstrap `$enable-rounded` SCSS variable.


#### Palette Fields

These fields use the `RGBColorField` field from [`django-colorful`](https://github.com/charettes/django-colorful).

- primary
- secondary
- success
- info
- warning
- danger
- white
- black
- light
- dark
- component_active_color
- component_active_bg


#### Option Fields

These fields use a `BooleanField`.

- enable_rounded
- enable_shadows
- enable_gradients


#### Typography Fields

These fields use a `CharField` unless otherwise noted.

- font_family_base
- font_size_base 
- line_height_base
- body_bg (`RGBColorField`)
- body_color (`RGBColorField`)


#### Headings Fields

These fields use a `CharField`

- headings_font_family
- headings_font_weight
- headings_line_height


### Non-Bootstrap Fields

#### CSS Storage Fields

These fields use a `TextField`

- css_above_the_fold
- css_below_the_fold


#### Utility Fields

- updated (`DateTimeField`)


## `SiteBootstrapTheme`

`bootstrap_customizer.models.SiteBootstrapTheme`

This model associates a `BootstrapTheme` with a specific [`Site`](https://docs.djangoproject.com/en/2.1/ref/contrib/sites/#django.contrib.sites.models.Site). An instance of this model is used by this package's [Views][views.md] and [Middleware][middleware.md].

### Fields

- bootstrap_theme (`ForeignKey(BootstrapTheme)`)
- site (`ForeignKey(Site)`)
