from django.contrib import admin

from music.models import Instrument, Epoch


class InstrumentAdmin(admin.ModelAdmin):
    ...


admin.site.register(Instrument, InstrumentAdmin)


class EpochAdmin(admin.ModelAdmin):
    ...


admin.site.register(Epoch, EpochAdmin)
