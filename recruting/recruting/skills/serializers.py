from rest_framework import serializers

from recruting.skills.models import Category, SkillQuestion, SkillSet, Position, Question


class CategorySerializer(serializers.ModelSerializer):
    department = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('id', 'department')


class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(required=True)

    class Meta:
        model = Question
        fields = ('id', 'question')


class PositionSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=True)
    department = CategorySerializer(required=False)

    class Meta:
        model = Position
        fields = ('id', 'status', 'department')


class SkillSetCreateSerializer(serializers.ModelSerializer):
    skill = serializers.CharField(required=True)

    class Meta:
        model = SkillSet
        fields = ('id', 'skill', 'position')


class SkillSetSerializer(serializers.ModelSerializer):
    skill = serializers.CharField(required=True)
    position = PositionSerializer()

    class Meta:
        model = SkillSet
        fields = ('id', 'skill', 'position')


class SkillSetQuestionSerializer(serializers.ModelSerializer):
    skill_set = SkillSetSerializer()
    question = QuestionSerializer()

    class Meta:
        model = SkillQuestion
        fields = ('id', 'skill_set', 'question')


class SkillSetQuestionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillQuestion
        fields = ('id', 'skill_set', 'question')