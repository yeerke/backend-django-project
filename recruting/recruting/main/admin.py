from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from recruting.main.models import Admin, Manager, Employee, EmployeeSkill, MyUser


@admin.register(MyUser)
class MyAdmin(UserAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'role')


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position')


@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'skill')

