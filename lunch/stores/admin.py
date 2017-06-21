from django.contrib import admin

# Register your models here.

# register Store
from django.contrib import admin
from .models import Store, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

#admin.site.register(Store)
# CASPER_NOTE : @admin.register <<< class method?
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes']
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']