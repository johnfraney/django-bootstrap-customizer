# Django Bootstrap Customizer

[
![PyPI](https://img.shields.io/pypi/v/django-bootstrap-customizer.svg)
![PyPI](https://img.shields.io/pypi/pyversions/django-bootstrap-customizer.svg)
![PyPI](https://img.shields.io/pypi/djversions/django-bootstrap-customizer.svg)
![PyPI](https://img.shields.io/pypi/l/django-bootstrap-customizer.svg)
](https://pypi.org/project/django-bootstrap-customizer/)


Django Bootstrap Customizer lets you build a custom Bootstrap theme by creating `BootstrapTheme` models from the Django admin.

`BootstrapTheme` values are converted to Bootstrap SCSS variables that are used to compile customized Bootstrap CSS when you save your theme, using [`libsass-python`](https://github.com/sass/libsass-python) under the hood.

Enjoy tailored Bootstrap CSS without having to set up a Node front-end assets pipeline!


## Features

* Bootstrap 4.
* Generates optimized above-the-fold and below-the-fold CSS payloads, perfect for improving your site's [Google PageSpeed](https://developers.google.com/speed/docs/insights/OptimizeCSSDelivery) score.
* Customized Bootstrap themes for each site in a [multi-site](https://docs.djangoproject.com/en/dev/ref/contrib/sites/#module-django.contrib.sites) installation.
* No Node/NPM/Gulp/Webpack required.

## Documentation

Documentation is available in the [docs directory](./docs/index.md) and at https://johnfraney.github.io/django-bootstrap-customizer.


## Credits

Tools used in rendering this package:

* [Bootstrap](https://github.com/twbs/bootstrap/)
* [libsass-python](https://github.com/sass/libsass-python)
* [django-colorful](https://github.com/charettes/django-colorful)
* [cssutils](https://pythonhosted.org/cssutils/index.html)
* [Cookiecutter](https://github.com/audreyr/cookiecutter)


## Code of Conduct

Everyone interacting in the project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).
