from django.db import models

from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='%(class)s_created_by',
        related_query_name='%(class)s_created_by',
        verbose_name='Creado por',
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='%(class)s_updated_by',
        related_query_name='%(class)s_updated_by',
        verbose_name='Actualizado por',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre de la compañía'
    )
    ruc = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='RUC',
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='Correo electrónico',
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        default='',
        verbose_name='Teléfono'
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Dirección'
    )
    primary_color = models.CharField(
        max_length=7,
        blank=True,
        default='',
        verbose_name='Color primario'
    )
    secondary_color = models.CharField(
        max_length=7,
        blank=True,
        default='',
        verbose_name='Color secundario'
    )
    # TODO: logo