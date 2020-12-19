from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.surname

class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудник'

