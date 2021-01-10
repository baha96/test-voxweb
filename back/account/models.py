from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    is_active = models.BooleanField(
        default=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    deleted = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    user_django = models.OneToOneField(
        User,
        related_name='additional',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user_django.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
