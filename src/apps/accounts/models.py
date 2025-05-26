from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    DNI = 'DNI'
    CE = 'CE'
    PASSPORT = 'PASSPORT'
    IDENTIFICATION_CHOICES = [
        (DNI, 'DNI'),
        (CE, 'CARNET DE EXTRANJERIA'),
        (PASSPORT, 'PASAPORTE'),
    ]
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Correo electrónico',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='¿Activo?'
    )
    names = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name='Nombres'
    )
    surnames = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name='Apellidos'
    )
    identification_type = models.CharField(
        choices=IDENTIFICATION_CHOICES,
        blank=True,
        verbose_name='Tipo de identificación',
        max_length=20,
    )
    vat = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Número de identificación'
    )
    timezone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Zona horaria',
        default=''
    )
    company = models.ForeignKey(
        to='core.Company',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='users',
        related_query_name='user',
        verbose_name='Compañía',
        db_index=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # TODO: image

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']

    def __str__(self):
        return f"{self.names} {self.surnames} ({self.email})"
