import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from recruting.main.models import MyUser, Admin, Manager, Employee
logger = logging.getLogger('log')


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        if instance.role == 1:
            Admin.objects.get_or_create(user=instance)
        elif instance.role == 2:
            Manager.objects.get_or_create(user=instance)
        else:
            Employee.objects.get_or_create(user=instance)

        logger.info(f"{instance.username}  Created!!!")
