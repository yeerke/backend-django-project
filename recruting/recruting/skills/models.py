from django.db import models


class Category(models.Model):
    department = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return f'{self.id}  {self.department}'


class Position(models.Model):
    status = models.CharField(max_length=255)
    department = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='positions')

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return f'id:{self.id},  status:{self.status},  depart:{self.department}'


class Question(models.Model):
    question = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f'id:{self.id}, question: {self.question}'


class SkillSet(models.Model):
    skill = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)

    class Meta:
        verbose_name = 'SkillSet'
        verbose_name_plural = 'SkillSets'

    def __str__(self):
        return f'id:{self.id}, skill: {self.skill}'


class SkillQuestion(models.Model):
    skill_set = models.ForeignKey(SkillSet, on_delete=models.CASCADE, related_name='skill_set')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name = 'SkillQuestion'
        verbose_name_plural = 'SkillQuestions'

    def __str__(self):
        return f'id: {self.id},  skill:{self.skill_set},  question:{self.question}'