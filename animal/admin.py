from django.contrib import admin

from animal.models import AnimalModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id' ,'name', 'breed', 'size', 'gender', 'color', 'observation', 'customer')
    list_display_links = ('id', 'name', 'breed',)
    search_fields = ('name', 'breed', 'size', 'customer', 'gender')
    list_filter = ('name', 'breed', 'size', 'customer', 'gender')
    ordering = ('customer', 'breed',)
    list_per_page =  25
admin.site.register(AnimalModel, ListCourse)