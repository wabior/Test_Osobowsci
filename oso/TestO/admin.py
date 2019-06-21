from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Pytanie)
# admin.site.register(Odp)
admin.site.register(Odp2)
admin.site.register(Wybory)

