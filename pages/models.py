from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from registration.models import Profile
from django_userforeignkey.models.fields import UserForeignKey


def custom_upload_to(instance, filename):
    return 'pages/' + filename

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    created_by = UserForeignKey(auto_user_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self):
        return self.title
