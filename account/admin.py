from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Worker, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)


class WorkerAdmin(
    UserAdmin
):  # Використовуємо UserAdmin для правильного керування користувачами
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "position",
    )
    fieldsets = UserAdmin.fieldsets + (  # Додаємо додаткові поля
        ("Додаткова інформація", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (  # Додаємо при створенні користувача
        ("Додаткова інформація", {"fields": ("position",)}),
    )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):  # Перевіряємо, чи введено новий пароль
            obj.set_password(form.cleaned_data["password"])  # Хешуємо пароль
        super().save_model(request, obj, form, change)


admin.site.register(Worker, WorkerAdmin)  # Реєструємо кастомного користувача
