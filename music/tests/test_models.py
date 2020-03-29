from django.test import TestCase
from music.models import Instrument, Epoch
from music.tests.factory import InstrumentFactory


class InstrumentTestCase(TestCase):
    def setUp(self):
        self.instrument = InstrumentFactory()

    def test_get_color_name(self):
        self.assertEqual(self.instrument.get_color_name, f"color 0 name 0")

    def test_get_color_name_with_none(self):
        self.instrument2 = InstrumentFactory(name="Test", color='')

        self.assertEqual(self.instrument2.get_color_name, f" Test")
