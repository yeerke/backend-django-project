from django.db import models


class Chat(models.Model):
    from_mes = models.CharField(max_length=255)
    to_mes = models.CharField(max_length=255)
    mess = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date', )
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.from_mes}-{self.mess}'