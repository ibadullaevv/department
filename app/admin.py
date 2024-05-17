from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models.users import CustomUser
from app.models.post import Post
from app.models.department import Department


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active', 'department')

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
    list_display = ('title', 'content', 'author')
