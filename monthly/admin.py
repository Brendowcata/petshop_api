from django.contrib import admin

from monthly.models import MonthlyModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'date_initial', 'date_final', 'value_money', 'amount_paid', 'scheduling_amount', 'customer', 'animal')
    list_display_links = ('id', 'date_initial', 'date_final')
    search_fields = ('animal', 'customer', 'date_initial', 'date_final',)
    list_filter = ('animal', 'customer', 'date_initial', 'date_final',)
    ordering = ('animal', 'customer',)
    list_per_page =  25
admin.site.register(MonthlyModel, ListCourse)