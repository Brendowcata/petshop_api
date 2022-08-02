from django.contrib import admin

from address.models import AddressModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id' ,'street', 'neighborhood', 'city', 'state', 'zip_code', 'house_number', 'customer')
    list_display_links = ('street', 'neighborhood',)
    search_fields = ('street', 'neighborhood', 'city', 'state', 'customer')
    list_filter = ('street', 'neighborhood', 'city', 'state', 'customer')
    ordering = ('customer',)
    list_per_page =  25
admin.site.register(AddressModel, ListCourse)