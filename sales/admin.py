from django.contrib import admin
from .models import Customer, Product, Bill, Order, Producttype

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']

    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "email_address", "account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter"],
            },
        ),
    ]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Producttype)