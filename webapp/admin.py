from django.contrib import admin
from webapp.models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'phone', 'created_date')
    list_filter = ('name',)
    search_fields = ('name', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)

