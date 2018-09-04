## Quickstart

Install Django Bootstrap Customizer:

```bash
pip install django-bootstrap-customizer
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'bootstrap_customizer',
    ...
)
```

Add URL patterns:

```python
from bootstrap_customizer import urls as bootstrap_customizer_urls


urlpatterns = [
    ...
    url(r'^', include(bootstrap_customizer_urls)),
    ...
]
```

## Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```
