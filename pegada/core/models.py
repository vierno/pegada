from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class AppUser(models.Model):
    class Meta:
        verbose_name = _('AppUser')
        verbose_name_plural = _('AppUsers')

    user = models.OneToOneField(User)

    shoe_size = models.IntegerField()

    right_foot = models.BooleanField()

    city = models.CharField(
        max_length=20
    )

    phone_number = models.CharField(
        max_length=15
    )

    def __unicode__(self):
        return self.user.username
