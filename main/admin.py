from django.contrib import admin

from .models import Conta, DebitoAutomatico

admin.site.register(Conta)
admin.site.register(DebitoAutomatico)
