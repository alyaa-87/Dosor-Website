from django.contrib import admin
from .models import Category
from .models import Line
from .models import Product
from .models import Order
from .models import Customer, Profile
from django.contrib.auth.models import User



admin.site.register(Category)
admin.site.register(Line)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)



# Mix profile and user infos
class ProfileInline(admin.StackedInline):
	model = Profile



# Extend User Model
class UserAdmin (admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]


# Unregister the old way and re-register the newway
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
