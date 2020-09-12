from django.contrib import admin

from core.models import Category, Service, Record


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fileds = '__all__'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Record)