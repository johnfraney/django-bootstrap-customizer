# FAQ

## Why is saving a `BootstrapTheme` so slow?

Short answer: it is difficult to add vendor-specific CSS property prefixes without using Node.

Bootstrap uses vendor-specific prefixes to add support for modern CSS features in a wider variety of browsers. Flexbox requires vendor-specific prefixes for IE10, for example. The Bootstrap SCSS code does not include any vendor-specific prefixes because they are added after-the-fact with an [`autoprefixer`](https://github.com/postcss/autoprefixer/) Node command. Because this plugin uses Python to compile SCSS into CSS, the compiled CSS doesn't include vendor-specific prefixes.

My solution was to use [`cssutils`](https://pythonhosted.org/cssutils/index.html) to parse Bootstrap's compiled CSS and extract only those CSS properties that used vendor-specific prefixes, then, using `cssutils` again, splice these properties into the `libsass`-compiled CSS. This process takes around 5 seconds on my AMD Ryzen 5 1600.

If you can think of a faster way to accomplish this, please [open an issue](https://github.com/johnfraney/django-bootstrap-customizer/issues/new) and let me know!
