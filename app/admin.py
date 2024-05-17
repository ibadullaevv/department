from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin

from app.models.users import CustomUser
from app.models.post import Post
from app.models.department import Department


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'department')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "department", "is_staff", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "department")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # def save_model(self, request, obj, form, change):
    #     if 'password' in form.cleaned_data:
    #         password = form.cleaned_data['password']
    #         obj.set_password(password)
    #         obj.save()
    #
    #     super().save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'author',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return qs

        return qs.filter(author=user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.department = request.user.department
        obj.save()

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            fields.remove('author')
            fields.remove('department')
        return fields
