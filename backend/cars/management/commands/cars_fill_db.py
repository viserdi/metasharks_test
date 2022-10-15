from django.core.management.base import BaseCommand

from .cars_fill import fill as cars_fill


class Command(BaseCommand):
    help = 'Заполнение базы авто.'

    def handle(self, *args, **options):

        cars_fill()
