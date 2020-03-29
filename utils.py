import os


def show_all_instruments():
    print(Instrument.objects.all())


if __name__ == '__main__':
    """Display all instruments queryset"""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alpha_project.settings")
    import django

    django.setup()
    from music.models import *

    show_all_instruments()
