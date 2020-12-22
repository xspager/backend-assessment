from django.contrib import admin

from .models import Customer, Partner, Activation


class CustomModelAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields_to_hide = ['deleted', 'active']
        fields = super().get_fields(request, obj)
        return [field for field in fields if field not in fields_to_hide]

    class Meta:
        abstract=True


class ActivationAdmin(CustomModelAdmin):
    list_display = ('__str__', 'created_at', 'status')
    list_filter = ('status',)
    readonly_fields = ('status', 'customer', 'partner')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Customer)
admin.site.register(Partner)
admin.site.register(Activation, ActivationAdmin)
