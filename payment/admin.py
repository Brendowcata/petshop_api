from django.contrib import admin

from payment.models import PaymentModel

class ListCourse(admin.ModelAdmin):
    list_display = ('id', 'value_money', 'amount_paid', 'payment_type', 'registration_date', 'pay_day')
    list_display_links = ('id', 'value_money',)
    search_fields = ('payment_type', 'registration_date', 'pay_day')
    list_filter = ('payment_type', 'registration_date', 'pay_day')
    ordering = ('id', 'registration_date', 'pay_day')
    list_per_page =  25
admin.site.register(PaymentModel, ListCourse)