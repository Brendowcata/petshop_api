from django.contrib import admin

from scheduling.models import SchedulingModel


class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'animal', 'date_appointment', 'hour_appointment',)
    list_display_links = ('id', 'animal',)
    search_fields = ('animal', 'date_appointment',)
    list_filter = ('animal', 'date_appointment',)
    ordering = ('animal',)
    list_per_page =  25
admin.site.register(SchedulingModel, ListCourse)