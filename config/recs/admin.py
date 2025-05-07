from django.contrib import admin
from recs.models import Record, Status, Type


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    # Админка для записей об операциях
    list_display = (
        "id",
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "summ",
        "comment",
    )

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    # Админка для статусов
    list_display = (
        "id",
        "name",
    )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    # Админка для типов
    list_display = (
        "id",
        "name",
    )

