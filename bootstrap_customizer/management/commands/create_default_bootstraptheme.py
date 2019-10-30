from django.core.management.base import BaseCommand, CommandError
from bootstrap_customizer.models import BootstrapTheme
from bootstrap_customizer.models import SiteBootstrapTheme

class Command(BaseCommand):
    help = 'Creates a BootstrapTheme and SiteBootstrapTheme if none exist'

    def handle(self, *args, **options):
        theme_count = BootstrapTheme.objects.count()
        if theme_count > 0:
            raise CommandError('A BootstrapTheme already exists')
        site_theme_count = SiteBootstrapTheme.objects.count()
        if theme_count > 0:
            raise CommandError('A SiteBootstrapTheme already exists')

        self.stdout.write('Creating BootstrapTheme and SiteBootstrapTheme')
        theme = BootstrapTheme()
        theme.save()
        site_theme = SiteBootstrapTheme(bootstrap_theme=theme, site_id=1)
        site_theme.save()

        self.stdout.write(self.style.SUCCESS('Successfully created BootstrapTheme'))

