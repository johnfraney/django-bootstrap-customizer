import cssutils
import logging
import os
import sass
from sys import platform
from django.conf import settings
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string


# Constants for OS path separator
POSIX_PATH_SEPARATOR = '/'
WINDOWS_PATH_SEPARATOR = '\\'

# Disable cssutils logging
cssutils.log.setLevel(logging.FATAL)
# Configure cssutils parsers to output minified CSS
cssutils.ser.prefs.useMinified()


def is_windows_environment():
    return platform == 'win32' or platform == 'cygwin'


def convert_fields_to_scss_variables(theme):
    """
    Converts the relevant fields from the supplied theme into a
    SCSS-compatible dict, e.g. {'$primary': '#007BFF'}
    """
    scss_fields = [f.name for f in theme._meta.fields if f.name not in theme.NON_SASS_FIELDS]
    scss_dict = dict()
    for f in scss_fields:
        scss_variable_name = '$' + f.replace('_', '-')
        scss_value = getattr(theme, f)
        # Make boolean values SCSS-friendly
        if type(scss_value) is bool:
            scss_value = 'true' if scss_value else 'false'
        scss_dict[scss_variable_name] = scss_value
    return scss_dict


def get_scss_template_context(theme):
    """
    Builds a context dict for populating a SCSS template for the
    given BootstrapTheme
    """
    bootstrap_scss_file_path = finders.find('bootstrap/scss/bootstrap.scss')
    bootstrap_scss_folder_path = os.path.dirname(os.path.abspath(bootstrap_scss_file_path))
    context = {}
    context['scss_variables'] = convert_fields_to_scss_variables(theme)
    context['STATIC_ROOT'] = settings.STATIC_ROOT
    context['bootstrap_scss_folder_path'] = bootstrap_scss_folder_path
    return context


def generate_above_the_fold_css(theme):
    """
    Returns a string containing above-the-fold Bootstrap CSS using the
    given BootstrapTheme
    """
    context = get_scss_template_context(theme)
    scss_string = render_to_string('bootstrap_customizer/bootstrap_above_the_fold.scss', context)
    if is_windows_environment():
        scss_string = scss_string.replace(WINDOWS_PATH_SEPARATOR, POSIX_PATH_SEPARATOR)
    return sass.compile(string=scss_string, output_style='compressed')


def generate_below_the_fold_css(theme):
    """
    Returns a string containing below-the-fold Bootstrap CSS using the
    given BootstrapTheme
    """
    context = get_scss_template_context(theme)
    scss_string = render_to_string('bootstrap_customizer/bootstrap_below_the_fold.scss', context)
    if is_windows_environment():
        scss_string = scss_string.replace(WINDOWS_PATH_SEPARATOR, POSIX_PATH_SEPARATOR)
    return sass.compile(string=scss_string, output_style='compressed')


def generate_full_css(theme):
    """
    Returns a string containing all Bootstrap CSS using the given
    BootstrapTheme
    """
    sass_variables = convert_fields_to_scss_variables(theme)
    variable_section = '\n'.join('{}: {};'.format(key, value) for key, value in sass_variables.items())
    bootstrap_import_section = '@import "{}";'.format(finders.find('bootstrap/scss/bootstrap.scss'))
    if is_windows_environment():
        bootstrap_import_section = bootstrap_import_section.replace(WINDOWS_PATH_SEPARATOR, POSIX_PATH_SEPARATOR)
    scss_string = '\n\n'.join([variable_section, bootstrap_import_section])
    return sass.compile(string=scss_string, output_style='compressed')


def extract_bootstrap_vendor_prefix_rules():
    """
    Returns vendor-prefixed properties from Bootstrap's compiled CSS
    """
    vendor_prefix_rules = {}
    bootstrap_css_file_path = finders.find('bootstrap/dist/css/bootstrap.min.css')
    parser = cssutils.CSSParser(validate=False)
    sheet = parser.parseString(open(bootstrap_css_file_path, 'r').read())
    vendor_prefix_rules = {}
    for rule in sheet:
        if not rule.type == rule.STYLE_RULE:
            continue
        for property in rule.style:
            if property.name.startswith('-'):
                if vendor_prefix_rules.get(rule.selectorText, None) is None:
                    vendor_prefix_rules[rule.selectorText] = []
                vendor_prefix_rules[rule.selectorText].append(property)

    return vendor_prefix_rules


def add_css_prefixes(css, vendor_prefix_rules):
    """
    Adds the supplied vendor prefix rules to the given CSS
    """
    selectors_with_vendor_prefixes = vendor_prefix_rules.keys()
    parser = cssutils.CSSParser(validate=False)
    sheet = parser.parseString(css)
    for rule in sheet:
        if not rule.type == rule.STYLE_RULE:
            continue
        if rule.selectorText not in selectors_with_vendor_prefixes:
            continue
        for property in vendor_prefix_rules[rule.selectorText]:
            rule.style[property.name] = property.value
    return sheet.cssText.decode()
