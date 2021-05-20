import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = 'Check db is available or not'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Waiting for database...'))
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    'Database unavailable, waiting for database to be ready.'
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
