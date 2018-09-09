from django.contrib import admin

from .models import BootstrapTheme, SiteBootstrapTheme


@admin.register(BootstrapTheme)
class BootstrapThemeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'name',
            )
        }),
        ('Options', {
            'fields': (
                'enable_rounded',
                'enable_shadows',
                'enable_gradients',
            )
        }),
        ('Palette', {
            'fields': (
                'primary',
                'secondary',
                'success',
                'info',
                'warning',
                'danger',
                'white',
                'black',
                'light',
                'dark',
                'component_active_color',
                'component_active_bg',
            )
        }),
        ('Typography', {
            'fields': (
                'font_family_base',
                'font_size_base',
                'line_height_base',
                'body_bg',
                'body_color',
            )
        }),
        ('Headings', {
            'classes': ('collapse',),
            'fields': (
                'headings_font_family',
                'headings_font_weight',
                'headings_line_height',
            )
        }),
    )


@admin.register(SiteBootstrapTheme)
class SiteBootstrapThemeAdmin(admin.ModelAdmin):
    list_display = ('site', 'bootstrap_theme')
