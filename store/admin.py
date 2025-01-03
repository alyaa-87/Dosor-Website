from django.contrib import admin
from .models import Category
from .models import Line
from .models import Product
from .models import Order
from .models import Customer, Profile, Feature, ProductFeature,Review
from django.contrib.auth.models import User



admin.site.register(Category)
admin.site.register(Line)
#admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)
#admin.site.register(Feature)
admin.site.register(ProductFeature)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
	search_fields=['name']


# Mix profile and user infos
class ProfileInline(admin.StackedInline):
	model = Profile



# Extend User Model
class UserAdmin (admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]


class ProductFeatureInline(admin.TabularInline):
	model = ProductFeature
	extra = 1 #no. of empty forms to display
	autocomplete_fields = ['feature']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	inlines = [ProductFeatureInline]
	list_display=['name','category','price']
	search_fields=['name', 'category__name']
	list_filter = ['category']

# Unregister the old way and re-register the newway
admin.site.unregister(User)
admin.site.register(User,UserAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']