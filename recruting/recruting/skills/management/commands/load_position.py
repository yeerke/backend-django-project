from django.core.management.base import BaseCommand

import linecache

from recruting.skills.models import Category, Position


class  Command(BaseCommand):

    def handle(self, *args, **options):
        path = 'data/departments.csv'
        departments = linecache.getlines(path)
        path = 'data/positions.csv'
        positions = linecache.getlines(path)
        for row in departments:
            row = row.rstrip("\n\r")
            try:
                c = Category.objects.get(department=row)
                self.stdout.write((self.style.WARNING(f"{c}")))
                for r in positions:
                    r = r.rstrip("\n\r")
                    try:
                        Position.objects.get_or_create(department=c, status=r)
                        self.stdout.write(self.style.SUCCESS(f"{r} position successful created"))
                    except Exception as g:
                        self.stdout.write(self.style.ERROR(f"{r} position is not created"))
                        print(g)
            except Exception as e:
                print(e)

