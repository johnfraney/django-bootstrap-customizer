from django import template
from bootstrap_customizer.models import BootstrapTheme
register = template.Library()


@register.simple_tag
def bootstrap_theme(theme_id):
    theme = BootstrapTheme.objects.get(id=theme_id)
    return theme.css
