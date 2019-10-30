from django import template
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.utils.safestring import mark_safe


register = template.Library()

missing_theme_message = (
    "Could not find a BootstrapTheme for this site. "
    "Create a BootstrapTheme entry in the admin or run "
    "the create_default_bootstraptheme management command."
)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_above_the_fold(context):
    try:
        bootstrap_theme = context['request'].bootstrap_theme
    except AttributeError:
        raise ImproperlyConfigured(missing_theme_message)
    return mark_safe(bootstrap_theme.css_above_the_fold)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_below_the_fold(context):
    try:
        bootstrap_theme = context['request'].bootstrap_theme
    except AttributeError:
        raise ImproperlyConfigured(missing_theme_message)
    return mark_safe(bootstrap_theme.css_below_the_fold)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_below_the_fold_url(context):
    try:
        bootstrap_theme = context['request'].bootstrap_theme
    except AttributeError:
        raise ImproperlyConfigured(missing_theme_message)
    return reverse('bootstrap_customizer:bootstrap_css_below_the_fold', kwargs=dict(
        hash=bootstrap_theme.get_hash()
    ))
