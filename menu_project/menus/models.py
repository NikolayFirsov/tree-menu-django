from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(verbose_name='Название меню', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название пункта', max_length=100)
    url = models.CharField(verbose_name='URL (прямой)', max_length=255, blank=True, null=True)
    named_url = models.CharField(verbose_name='Именованный URL', max_length=255, blank=True, null=True)
    menu = models.ForeignKey(Menu, verbose_name='Меню', related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт',
        blank=True, null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(verbose_name='Порядок', default=0)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def clean(self):
        if not self.url and not self.named_url:
            raise ValidationError('Необходимо указать либо URL, либо Именованный URL.')
        if self.url and self.named_url:
            raise ValidationError('Нельзя одновременно указать и URL, и Именованный URL. Выберите одно.')

