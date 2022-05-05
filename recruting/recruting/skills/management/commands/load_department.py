from django.core.management.base import BaseCommand

import linecache

from recruting.skills.models import Category


class  Command(BaseCommand):

    def handle(self, *args, **options):
        path = 'data/departments.csv'
        departments = linecache.getlines(path)
        for row in departments:
            row = row.rstrip("\n\r")
            try:
                Category.objects.get_or_create(department=row)
                print(row, 'department is created!!!')
            except Exception as e:
                print(row, 'this one is not created')
                print(e)
        print('Finished load departments!!')
