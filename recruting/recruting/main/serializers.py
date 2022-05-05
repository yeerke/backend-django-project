from rest_framework import serializers

from recruting.main.models import MyUser, Admin, Manager, Employee, EmployeeSkill
from recruting.skills.serializers import SkillSetSerializer, CategorySerializer, PositionSerializer


class MyUserShortSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username')


class MyUserFullSerializer(MyUserShortSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta(MyUserShortSerializer.Meta):
        fields = MyUserShortSerializer.Meta.fields + ('password', 'first_name', 'last_name', 'email', 'role')

    def validate_password(self, pswd):
        if len(pswd) < 5:
            raise serializers.ValidationError('Password length should be more than 5')
        return pswd


class AdminSerializer(serializers.ModelSerializer):
    user = MyUserFullSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = ('id', 'user')


class ManagerSerializer(serializers.ModelSerializer):
    user = MyUserFullSerializer(required=True)
    department = CategorySerializer(required=True)

    class Meta:
        model = Manager
        fields = ('id', 'department', 'user')


class EmployeeSerializer(serializers.ModelSerializer):
    user = MyUserFullSerializer(required=True)
    position = PositionSerializer(required=True)

    class Meta:
        model = Employee
        fields = ('id', 'position', 'user')


class EmployeeSkillSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)
    skill = SkillSetSerializer(required=True)

    class Meta:
        model = EmployeeSkill
        fields = ('id', 'employee', 'skill')
