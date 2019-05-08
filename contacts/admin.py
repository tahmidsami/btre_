from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    #list_editable = ('is_published',)
    search_fields = ('name', 'listing', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)