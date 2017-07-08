from django.db import models
from django.contrib.auth.models import User

# Профиль юзера
class Profile(models.Model):
    user = models.ForeignKey(User)
    middle_name = models.CharField(verbose_name="Отчество", max_length=45, blank=True)
    sex = models.NullBooleanField(verbose_name='Пол', null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    userpic = models.ImageField(upload_to='media/userpics/', blank=True)