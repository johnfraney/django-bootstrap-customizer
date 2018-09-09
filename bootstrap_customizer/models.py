import hashlib
import sass
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from colorful.fields import RGBColorField

from . import constants
from .utils import (
    add_css_prefixes,
    extract_bootstrap_vendor_prefix_rules,
    generate_above_the_fold_css,
    generate_below_the_fold_css,
    generate_full_css
)


class BootstrapTheme(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Short name used to identify this theme",
    )
    # Palette
    primary = RGBColorField(default=constants.BLUE)
    secondary = RGBColorField(default=constants.GRAY_600)
    success = RGBColorField(default=constants.GREEN)
    info = RGBColorField(default=constants.CYAN)
    warning = RGBColorField(default=constants.YELLOW)
    danger = RGBColorField(default=constants.RED)
    white = RGBColorField(default=constants.WHITE)
    black = RGBColorField(default=constants.BLACK)
    light = RGBColorField(default=constants.GRAY_100)
    dark = RGBColorField(default=constants.GRAY_800)

    component_active_color = RGBColorField(default=constants.WHITE)
    component_active_bg = RGBColorField("component active background", default=constants.BLUE)

    # Options
    enable_rounded = models.BooleanField(default=True)
    enable_shadows = models.BooleanField(default=False)
    enable_gradients = models.BooleanField(default=False)

    # Typography
    font_family_base = models.CharField(
        max_length=250,
        default=constants.FONT_FAMILY_SANS_SERIF,
    )
    font_size_base = models.CharField(max_length=100, default='1rem')
    line_height_base = models.CharField(max_length=100, default='1.5')
    body_bg = RGBColorField('body background', default=constants.WHITE)
    body_color = RGBColorField(default=constants.GRAY_900)

    # Headings
    headings_font_family = models.CharField(max_length=250, default='inherit')
    headings_font_weight = models.CharField(max_length=250, default='500')
    headings_line_height = models.CharField(max_length=250, default='1.2')

    css_above_the_fold = models.TextField(blank=True, default='')
    css_below_the_fold = models.TextField(blank=True, default='')

    updated = models.DateTimeField(auto_now=True)

    NON_SASS_FIELDS = [
        'css',
        'css_above_the_fold',
        'css_below_the_fold',
        'id',
        'name',
        'updated',
    ]

    def clean(self):
        try:
            generate_full_css(self)
        except sass.CompileError as err:
            raise ValidationError(err)

    def save(self, *args, **kwargs):
        vendor_prefix_rules = extract_bootstrap_vendor_prefix_rules()
        self.css_above_the_fold = add_css_prefixes(generate_above_the_fold_css(self), vendor_prefix_rules)
        self.css_below_the_fold = add_css_prefixes(generate_below_the_fold_css(self), vendor_prefix_rules)
        super(BootstrapTheme, self).save(*args, **kwargs)

    def get_hash(self):
        unique_string = '{}-{}'.format(self.id, self.updated.timestamp())
        return hashlib.md5(unique_string.encode()).hexdigest()

    class Meta:
        verbose_name = 'Bootstrap theme'

    def __str__(self):
        return self.name


class SiteBootstrapTheme(models.Model):
    site = models.OneToOneField(Site, null=True, on_delete=models.SET_NULL)
    bootstrap_theme = models.ForeignKey(BootstrapTheme, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'site Bootstrap theme'
