from django.core.management.base import BaseCommand, CommandError

from music.models import Instrument, Musician


class Command(BaseCommand):
    help = 'Test command'

    # def add_arguments(self, parser):
    #     parser.add_argument('instr_id', nargs='+', type=int)

    @staticmethod
    def show_all_instruments(instr_id):
        print(Instrument.objects.filter(id__in=instr_id))

    @staticmethod
    def generate_musician():
        musician = Musician.objects.create(first_name='Test', last_name='Test', bio='Test')
        print(musician.alive)

    def handle(self, *args, **options):
        self.generate_musician()


