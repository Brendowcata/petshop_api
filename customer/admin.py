from django.contrib import admin

from customer.models import CustomerModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email', 'telephone', 'phone_number')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cpf', 'email',)
    list_filter = ('name', 'cpf', 'email',)
    ordering = ('name',)
    list_per_page =  25
admin.site.register(CustomerModel, ListCourse)