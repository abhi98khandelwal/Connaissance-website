from django.contrib import admin
from .models import PEvent, WEvent
# Register your models here.

admin.site.register(WEvent)
admin.site.register(PEvent)