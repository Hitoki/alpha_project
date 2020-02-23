from django.contrib import admin

from music.models import Instrument, Epoch, Musician


class InstrumentAdmin(admin.ModelAdmin):
    ...


class EpochAdmin(admin.ModelAdmin):
    ...


class MusicianAdmin(admin.ModelAdmin):
    ...


admin.site.register(Epoch, EpochAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Musician, MusicianAdmin)

