from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User


# Register your models here
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)


#create an OrderItem inline
class OrderItemInline(admin.StackedInline):
	model = OrderItem
	extra = 0


#extend our order model
class OrderAdmin(admin.ModelAdmin):
	model = Order
	readonly_fields = ['date_ordered']
	#fields =["full_name",...] if I want to show certain stuff in the model and not all of them
	inlines = [OrderItemInline]


admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)