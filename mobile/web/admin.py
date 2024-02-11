from django.contrib import admin
from . models import Product,Order,OrderItem
from . models import from_date
from . models import contact_date
from . models import Leave

# Register your models here.
class OrderItemTubleInline(admin.TabularInline):
    model=OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubleInline]

admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

admin.site.register(from_date)

admin.site.register(contact_date)

admin.site.register(Leave)