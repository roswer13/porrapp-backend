
"""
Database models.
"""
import os
import time
import io

from PIL import Image as PILImage
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile


def logo_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    timestamp = int(time.time() * 1000)
    name_slug = slugify(instance.name)
    return f'competitions/{name_slug}/logo_{timestamp}{ext}'


class Competition(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Name of the competition'),
        max_length=128
    )
    year = models.PositiveIntegerField(
        verbose_name=_('Year'),
        help_text=_('Year of the competition'),
        default=2024
    )
    host_country = models.CharField(
        verbose_name=_('Host Country'),
        help_text=_('Country hosting the competition'),
        max_length=128,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        upload_to=logo_upload_path,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At')
    )

    def save(self, *args, **kwargs):
        if self.logo:
            img = PILImage.open(self.logo)
            img.thumbnail((800, 800), PILImage.Resampling.LANCZOS)
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=85)
            img_file = ContentFile(img_io.getvalue(), name=self.logo.name)
            self.logo = img_file

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name