from django.contrib.auth.models import Group
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

from .models import Profile



@receiver(post_save, sender=Profile)
def add_user_to_teraphy_group(sender, instance, created, **kwargs):
    if created:
        try:
            teraphist = Group.objects.get(name='terapeutas')
        except Group.DoesNotExist:
            teraphist = Group.objects.create(name='terapeutas')
            patients = Group.objects.create(name='pacientes')
            administrators = Group.objects.create(name='administradores')

        instance.user.groups.add(teraphist)
