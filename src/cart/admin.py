from django.contrib import admin
from .models import (
    Producto, 
    Order, 
    OrderItem, 
    Medida,
    Address,
    Payment,
    Category
)

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_1',
        'address_line_2',
        'city',
        'address_type',
    ]

admin.site.register(Producto)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Medida)
admin.site.register(Payment)
admin.site.register(Category)