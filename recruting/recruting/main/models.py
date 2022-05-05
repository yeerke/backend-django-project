import os

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser

from recruting.skills.models import Position, SkillSet, Category

from rest_framework import serializers


MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.doc', '.pdf']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise serializers.ValidationError(f'max file size is: {MAX_FILE_SIZE}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


def validate_role(value):
    if 3 < value < 0:
        return serializers.ValidationError('invalid number of Role')


class MyUser(AbstractUser):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER, 'manager'),
        (EMPLOYEE, 'employee')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, validators=[validate_role])

    def __str__(self):
        return f'({self.id}) {self.username} {self.first_name} {self.last_name}'


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='admin_photo', validators=[validate_extension, validate_file_size],
                              blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.user}'


class Manager(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='manager_photo', validators=[validate_extension, validate_file_size],
                              blank=True, null=True)

    def __str__(self):
        return f'Manager: {self.id} {self.user} {self.department}'


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='positions', blank=True, null=True)
    photo = models.ImageField(upload_to='employee_photo', validators=[validate_extension, validate_file_size],
                              blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'Employee: {self.id} {self.user} {self.position}'


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(SkillSet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee} {self.skill}'

