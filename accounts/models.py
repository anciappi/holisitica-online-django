from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

#PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    birthday = models.DateField(null=True, blank=True, verbose_name='fecha de nacimiento')
    image = models.ImageField(default='user/usuario_defecto.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    country = models.CharField(max_length=40, null=True, blank=True, verbose_name='Pais')
    location = models.CharField(max_length=40, null=True, blank=True, verbose_name='Provincia')
    celphone = models.CharField(max_length=40, null=True, blank=True, verbose_name='Celular')
    instagram = models.CharField(max_length=40, null=True, blank=True, verbose_name='Instagram')
    facebook = models.CharField(max_length=40, null=True, blank=True, verbose_name='Facebook')

    THERAPHYS = (
        ('reiki', 'Reiki'),
        ('memoria', 'Memoria Celular'),
        ('meditacion', 'Meditación'),
        ('Yoga', 'Yoga'),
    )
    theraphys = models.CharField(max_length=60, choices=THERAPHYS, null=True, blank=True, verbose_name='Terapias')
    description = models.TextField(null=True, blank=True, verbose_name='descripción')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['id']

    def __str__(self):
        return self.user.username
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

