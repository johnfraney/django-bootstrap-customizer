from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_above_the_fold(context):
    bootstrap_theme = context['request'].bootstrap_theme
    return mark_safe(bootstrap_theme.css_above_the_fold)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_below_the_fold(context):
    bootstrap_theme = context['request'].bootstrap_theme
    return mark_safe(bootstrap_theme.css_below_the_fold)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_below_the_fold_url(context):
    bootstrap_theme = context['request'].bootstrap_theme
    return reverse('bootstrap_customizer:bootstrap_css_below_the_fold', kwargs=dict(
        hash=bootstrap_theme.get_hash()
    ))
