import sass
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django.db import models
from colorful.fields import RGBColorField

from . import colours


class BootstrapTheme(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(
        max_length=200, primary_key=True,
        help_text="Short name used to identify this theme"
    )
    # Palette
    primary = RGBColorField(default=colours.BLUE)
    secondary = RGBColorField(default=colours.GRAY_600)
    success = RGBColorField(default=colours.GREEN)
    info = RGBColorField(default=colours.CYAN)
    warning = RGBColorField(default=colours.YELLOW)
    danger = RGBColorField(default=colours.RED)
    white = RGBColorField(default=colours.WHITE)
    black = RGBColorField(default=colours.BLACK)
    light = RGBColorField(default=colours.GRAY_100)
    dark = RGBColorField(default=colours.GRAY_800)

    component_active_color = RGBColorField(default=colours.WHITE)
    component_active_bg = RGBColorField("component active background", default=colours.BLUE)

    # Options
    enable_rounded = models.BooleanField(default=True)
    enable_shadows = models.BooleanField(default=False)
    enable_gradients = models.BooleanField(default=False)

    # Typography
    font_family_base = models.CharField(
        max_length=250,
        default=colours.FONT_FAMILY_SANS_SERIF,
    )
    font_size_base = models.CharField(max_length=100, default='1rem')
    line_height_base = models.CharField(max_length=100, default='1.5')
    body_bg = RGBColorField('body background', default=colours.WHITE)
    body_color = RGBColorField(default=colours.GRAY_900)

    # Headings
    headings_font_family = models.CharField(max_length=250, default='inherit')
    headings_font_weight = models.CharField(max_length=250, default='500')
    headings_line_height = models.CharField(max_length=250, default='1.2')

    css = models.TextField()

    def clean(self):
        try:
            self.generate_css()
        except sass.CompileError as err:
            raise ValidationError(err)

    def get_sass_variables(self):
        non_sass_fields = ['css', 'id', 'name']
        sass_fields = [f.name for f in self._meta.fields if f.name not in non_sass_fields]
        sass_dict = dict()
        for f in sass_fields:
            sass_variable_name = '$' + f.replace('_', '-')
            sass_value = getattr(self, f)
            # Make boolean values to SCSS-friendly
            if type(sass_value) is bool:
                sass_value = 'true' if sass_value else 'false'
            sass_dict[sass_variable_name] = sass_value
        return sass_dict

    def generate_css(self):
        bootstrap_scss_file_path = finders.find('bootstrap/scss/bootstrap.scss')
        sass_variables = self.get_sass_variables()
        variable_section = '\n'.join('{}: {};'.format(key, value) for key, value in sass_variables.items())
        bootstrap_import_section = '@import "{}";'.format(bootstrap_scss_file_path)
        sass_string = '\n\n'.join([variable_section, bootstrap_import_section])
        return sass.compile(string=sass_string, output_style='compressed')

    class Meta:
        verbose_name = 'Bootstrap theme'

    def save(self, *args, **kwargs):
        self.css = self.generate_css()
        super(BootstrapTheme, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
