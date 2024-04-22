from django.contrib import admin

# Register your models here.
from .models import Location, Department, Category, SubCategory, SKUData

admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SKUData)
