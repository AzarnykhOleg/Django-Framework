from django.contrib import admin
from .models import Client, Product, Order
from django.utils.translation import gettext as _


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address']
    list_display_links = ('name', 'email')
    ordering = ['name', '-date_of_registration']
    list_editable = ('phone_number',)
    list_filter = ['date_of_registration']
    list_per_page = 10
    search_fields = ['name']
    search_help_text = 'Поиск по полю ИМЯ КЛИЕНТА'


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    count = queryset.update(quantity=0)
    modeladmin.message_user(request, f"Вы обнулили {count} записи(ей).")


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'image']
    ordering = ['title', '-price']
    # list_editable = ('quantity',)
    list_filter = ['price', 'date_of_addition']
    # list_per_page = 10
    search_fields = ['description']
    search_help_text = 'Поиск по полю ОПИСАНИЕ'
    actions = [reset_quantity]

    readonly_fields = ['date_of_addition']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Description',
            {
                'classes': ['collapse'],
                'description': 'Товар и его подробное описание',
                'fields': ['description', 'date_of_addition', 'image'],
            },
        ),
        (
            'Other',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    ordering = ['total_price']
    list_filter = ['total_price', 'customer']
    list_per_page = 10


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
