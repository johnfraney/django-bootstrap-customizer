# Template Tags

The template tags in the library help get your customized Bootstrap CSS into your templates.

To use these template tags, be sure to load the `bootstrap_customizer` template tag library:

```html+django
{% load bootstrap_customizer %}
```

## `bootstrap_theme_css_above_the_fold`

Outputs the CSS from the current site's `BootstrapTheme.css_above_the_fold` field as a string.

### Usage

```html+django
<style lang="css">{% bootstrap_theme_css_above_the_fold %}</style>
```

## `bootstrap_theme_css_below_the_fold`

Outputs the CSS from the current site's `BootstrapTheme.css_below_the_fold` field as a string.

### Usage

```html+django
<style lang="css">{% bootstrap_theme_css_below_the_fold %}</style>
```

## `bootstrap_theme_css_below_the_fold_url`

Outputs a URL to [`CSSBelowTheFoldView`](views.md#cssbelowthefoldview), using a hash from the current site's [`BootstrapTheme`](models.md#bootstraptheme).

### Usage

```html+django
<link rel="stylesheet" href="{% bootstrap_theme_css_below_the_fold_url %}">
```
