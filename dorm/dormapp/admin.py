from django.contrib import admin
from dormapp.models import Record
# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('college', 'note', 'IPadd', 'IPdelete')
admin.site.register(Record, RecordAdmin)
