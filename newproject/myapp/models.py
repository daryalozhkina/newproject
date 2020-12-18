from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return self.surname


    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студент'


class Groups(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Студенты группы'
        verbose_name_plural = 'Студент группы'