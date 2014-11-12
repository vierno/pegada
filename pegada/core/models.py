from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from localflavor.br.br_states import STATE_CHOICES


class AppUser(models.Model):
    class Meta:
        verbose_name = _('AppUser')
        verbose_name_plural = _('AppUsers')

    user = models.OneToOneField(User)

    shoe_size = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    foot = models.CharField(
        null=False,
        blank=False,
        max_length=1,
        choices=(
            ("r", _("right")),
            ("l", _("left")),
        ),
    )

    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
    )

    city = models.CharField(
        max_length=20
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return self.user.username


class Shoe(models.Model):
    class Meta:
        verbose_name = "Shoe"
        verbose_name_plural = "Shoes"

    def __unicode__(self):
        return u"{0} - {1} - {2}".format(self.app_user, self.size, self.title)

    title = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )

    size = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    foot = models.CharField(
        null=False,
        blank=False,
        max_length=1,
        choices=(
            ("r", _("right")),
            ("l", _("left")),
        ),
    )

    app_user = models.ForeignKey(
        "AppUser",
        null=False,
        blank=False,
    )
