from django.contrib import admin

from monthly.models import MonthlyModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'date_initial', 'date_final', 'payment', 'scheduling_amount', 'pet')
    list_display_links = ('id', 'date_initial', 'date_final')
    search_fields = ('pet', 'date_initial', 'date_final',)
    list_filter = ('pet', 'date_initial', 'date_final',)
    ordering = ('pet',)
    list_per_page =  25
admin.site.register(MonthlyModel, ListCourse)