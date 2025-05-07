from django.contrib import admin
from categorys.models import Category, Sub_Category


# Админка для категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "type"
    )


# Админка для подкатегорий
@admin.register(Sub_Category)
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category"
    )
