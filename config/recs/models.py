from django.db import models


class Status(models.Model):
    # Модель "Статус"
    name = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        # Отображение модели
        return f'{self.name}'

    class Meta:
        # Отображение наименования модели
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    # Модель "Тип"
    name = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Record(models.Model):
    # Модель записи
    created_at = models.DateTimeField(verbose_name='Дата создания записи')
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, verbose_name='Тип операции', on_delete=models.CASCADE)
    category = models.ForeignKey('categorys.Category', verbose_name='Категория', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('categorys.Sub_Category', verbose_name='Подкатегория', on_delete=models.CASCADE)
    summ = models.FloatField(verbose_name='Сумма')
    comment = models.CharField(max_length=150, verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.created_at} {self.type}'

    class Meta:
        verbose_name = 'Запись о переводе'
        verbose_name_plural = 'Записи о переводах'
