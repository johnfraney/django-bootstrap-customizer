# Advanced Usage

**Note**: For basic usage, see the [Quickstart section of the Home page](index.md#quickstart).

## Introduction

Django Bootstrap Customizer was built to make it easy to compile and serve Bootstrap CSS in Django, and to facilitate serving that CSS efficiently.

This page will show you how to use features of Django and Django Bootstrap Customizer to optimize your CSS delivery, using strategies from [Google's PageSpeed Tools Insights](https://developers.google.com/speed/docs/insights/OptimizeCSSDelivery).


## Above-the-fold/Critical CSS

Critical, above-the-fold CSS is stored in a `BootstrapTheme`'s `css_above_the_fold` field.

To improve load times and reduce database usage, the above-the-fold CSS should be inlined and placed in a [`cache` template tag](https://docs.djangoproject.com/en/dev/topics/cache/#template-fragment-caching).

First, install the Django Bootstrap Customizer `BootstrapThemeMiddleware` middleware, after Django's `CurrentSiteMiddleware`:

```python

MIDDLEWARE = [
    ...
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'bootstrap_customizer.middleware.BootstrapThemeMiddleware',
    ...
]
```

This middleware adds a `request.bootstrap_theme` attribute containing the current site's `BootstrapTheme`. We can use this to refresh the following cached template fragment so that we always see the most up-to-date version of our Bootstrap themes.

```html
{% load bootstrap_customizer cache %}

<head>
  {% cache 600 css-above-the-fold request.site request.bootstrap_theme.updated %}
    <style lang="css">{% bootstrap_theme_css_above_the_fold %}</style>
  {% endcache %}
</head>
```

Let's look at the argments to the cache tag:

| Argument                          | Description                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------|
| `600`                             | Timeout. The cache fragment will time out after 10 minutes                              |
| `css-above-the-fold`              | Cache fragment name, in `kebab-case` to distinguish it from a template context variable |
| `request.site`                    | Make fragment unique for each site                                                      |
| `request.bootstrap_theme.updated` | Make fragment unique for each version of a `BootstrapTheme`                             |


## Below-the-fold/Deferred CSS

Non-critical, below-the-fold CSS is stored in a `BootstrapTheme`'s `css_below_the_fold` field and served via `bootstrap_customizer.views.CSSBelowTheFoldView`, which leverages [view caching](https://docs.djangoproject.com/en/dev/topics/cache/#the-per-view-cache).

Google [recommends](https://developers.google.com/speed/docs/insights/OptimizeCSSDelivery#recommendations) using JavaScript to load below-the-fold CSS after the DOM has finished loading (i.e., after the `load` event has fired). This speed up page loads because "styles are applied to the page once it finishes loading, without blocking the initial render of the critical content."

Here's how to defer loading of below-the-fold CSS:

```html
<body>
  <!-- Adapted from https://developers.google.com/speed/docs/insights/OptimizeCSSDelivery -->
  <noscript id="deferred-styles">
    <link rel="stylesheet" type="text/css" href="{% bootstrap_theme_css_below_the_fold_url %}">
  </noscript>
  <script>
    var loadDeferredStyles = function() {
      var addStylesNode = document.getElementById("deferred-styles");
      var replacement = document.createElement("div");
      replacement.innerHTML = addStylesNode.textContent;
      document.body.appendChild(replacement)
      addStylesNode.parentElement.removeChild(addStylesNode);
    };
    var raf = requestAnimationFrame || mozRequestAnimationFrame ||
        webkitRequestAnimationFrame || msRequestAnimationFrame;
    if (raf) raf(function() { window.setTimeout(loadDeferredStyles, 0); });
    else window.addEventListener('load', loadDeferredStyles);
  </script>
</body>
```

