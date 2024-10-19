from django.contrib import admin
from .models import Branch, Product, Inventory, SalesAccount, ClientAccount, Order, OrderItem

admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(SalesAccount)
admin.site.register(ClientAccount)
admin.site.register(Order)
admin.site.register(OrderItem)
