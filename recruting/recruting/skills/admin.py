from django.contrib import admin

from recruting.skills.models import Category, SkillSet, SkillQuestion, Position, Question


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'department')


@admin.register(SkillSet)
class SkillSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'position')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'department')


@admin.register(SkillQuestion)
class SkillQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_set', 'question')


@admin.register(Question)
class SkillQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


