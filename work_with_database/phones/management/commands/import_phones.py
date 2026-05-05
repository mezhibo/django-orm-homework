import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **options):
        with open('phones.csv', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')

            for row in reader:
                Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'price': int(row['price']),
                        'image': row['image'],
                        'release_date': datetime.strptime(
                            row['release_date'],
                            '%Y-%m-%d'
                        ).date(),
                        'lte_exists': row['lte_exists'] == 'True',
                    }
                )

        self.stdout.write(self.style.SUCCESS('Phones imported successfully'))
