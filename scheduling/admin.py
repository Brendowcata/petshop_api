from django.contrib import admin

from scheduling.models import SchedulingModel


class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'pet', 'date_appointment', 'hour_appointment',)
    list_display_links = ('id', 'pet',)
    search_fields = ('pet', 'date_appointment',)
    list_filter = ('pet', 'date_appointment',)
    ordering = ('pet',)
    list_per_page =  25
admin.site.register(SchedulingModel, ListCourse)