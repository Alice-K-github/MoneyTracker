from django.db import models


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    type = models.ForeignKey('recs.Type', verbose_name='Тип', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.type})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Модель подкатегории
class Sub_Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
