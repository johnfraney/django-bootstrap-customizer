from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.safestring import mark_safe

from bootstrap_customizer.models import SiteBootstrapTheme


register = template.Library()


@register.simple_tag
def bootstrap_theme_css_above_the_fold():
    site_theme = SiteBootstrapTheme.objects.select_related('bootstrap_theme').get(
        site_id=get_current_site(None)
    )
    return mark_safe(site_theme.bootstrap_theme.css_above_the_fold)


@register.simple_tag
def bootstrap_theme_css_below_the_fold():
    site_theme = SiteBootstrapTheme.objects.select_related('bootstrap_theme').get(
        site_id=get_current_site(None)
    )
    return mark_safe(site_theme.bootstrap_theme.css_below_the_fold)


@register.simple_tag(takes_context=True)
def bootstrap_theme_css_below_the_fold_url(context):
    bootstrap_theme = context['request'].bootstrap_theme
    return reverse('bootstrap_customizer:bootstrap_css_below_the_fold', kwargs=dict(
        hash=bootstrap_theme.get_hash()
    ))
