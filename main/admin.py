from django.contrib import admin

from .models import Customer, Partner, Activation

class ActivationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'status')
    list_filter = ('status',)

admin.site.register(Customer)
admin.site.register(Partner)
admin.site.register(Activation, ActivationAdmin)
