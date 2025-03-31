from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    """Admin configuration for OrderItem inline display."""
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product']}),
        ('Quantity', {'fields': ['quantity']}),
        ('Price', {'fields': ['price']}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0


class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for Order model."""
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = [
        'id', 'token', 'total', 'emailAddress', 'created', 
        'billingName', 'billingAddress1', 'billingCity', 
        'billingPostcode', 'billingCountry', 'shippingName', 
        'shippingAddress1', 'shippingCity', 'shippingPostcode', 
        'shippingCountry'
    ]
    fieldsets = [
        ('ORDER INFORMATION', {
            'fields': ['id', 'token', 'total', 'created']
        }),
        ('BILLING INFORMATION', {
            'fields': [
                'billingName', 'billingAddress1', 'billingCity', 
                'billingPostcode', 'billingCountry'
            ]
        }),
        ('SHIPPING INFORMATION', {
            'fields': [
                'shippingName', 'shippingAddress1', 'shippingCity', 
                'shippingPostcode', 'shippingCountry'
            ]
        }),
    ]
    inlines = [OrderItemAdmin]

    def has_delete_permission(self, request, obj=None):
        """Disable delete permission for Order model."""
        return False

    def has_add_permission(self, request):
        """Disable add permission for Order model."""
        return False


# Register the Order model with the custom admin configuration
admin.site.register(Order, OrderAdmin)