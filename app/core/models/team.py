import os
import time
import io

from PIL import Image as PILImage
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from core.models import Competition


def logo_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    timestamp = int(time.time() * 1000)
    name_slug = slugify(instance.name)
    return f'teams/{name_slug}/logo_{timestamp}{ext}'


class Team(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        help_text=_('Name of the team'),
        max_length=128
    )
    flag = models.ImageField(
        upload_to=logo_upload_path,
        blank=True,
        null=True
    )
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='teams',
        verbose_name=_('Competition'),
        help_text=_('Competition this team belongs to')
    )

    def save(self, *args, **kwargs):
        if self.flag:
            img = PILImage.open(self.flag).convert("RGBA")

            datas = img.getdata()
            new_data = []
            for item in datas:
                if item[0] > 240 and item[1] > 240 and item[2] > 240:
                    new_data.append((255, 255, 255, 0))  # transparente
                else:
                    new_data.append(item)

            img.putdata(new_data)

            img.thumbnail((800, 800), PILImage.Resampling.LANCZOS)

            img_io = io.BytesIO()
            img.save(img_io, format="PNG", optimize=True)
            new_name = f"{os.path.splitext(self.flag.name)[0]}.png"

            self.flag.save(new_name, ContentFile(img_io.getvalue()), save=False)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name