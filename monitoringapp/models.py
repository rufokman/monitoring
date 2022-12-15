from django.db import models
from django.utils import timezone

class Config(models.Model):
    allow_edit = models.BooleanField(default=True)
    last_download = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'config'


class Card(models.Model):
    status_list = [(0, 'Согласован'),
                   (1, 'Согласование СУП'),
                   (2, 'На доработке'),
                   (3, 'Новый')]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='Последнее обновление')
    status = models.PositiveIntegerField(choices=status_list, default=3, verbose_name="Статус")
    send = models.BooleanField(default=False, verbose_name="Выбрать все")
    name_of_user = models.TextField(verbose_name='ФИО пользователя')
    organization = models.CharField(verbose_name="Организация", max_length=300)
    role = models.CharField(max_length=1000, verbose_name="Должность")
    fio = models.CharField(max_length=1000, verbose_name="ФИО сотрудника, в чью карту устанавливается КПЭ")
    id_kpi = models.CharField(max_length=300, verbose_name='Идентификатор КПЭ', default='-')
    type = models.CharField(max_length=100, verbose_name='КПЭ/КлС', default='-')
    name = models.CharField(max_length=1000, verbose_name='Наименование КПЭ / КлС')
    method = models.CharField(max_length=1000, verbose_name='Методика расчета')
    low_level = models.CharField(max_length=3000, verbose_name='Нижний уровень')
    target_level = models.CharField(max_length=3000, verbose_name='Целевой уровень')
    high_level = models.CharField(max_length=3000, verbose_name="Верхний уровень")
    weight = models.IntegerField(verbose_name='Вес')
    first_quarter=models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 1 кв')
    second_quarter=models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 2 кв')
    third_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 3 кв')
    fourth_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 4 кв')
    reason = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Причина отклонения')
    measure = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Предпринимаемые меры')
    forecast = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Прогнозное значение')
    verificator = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Верификатор')
    delete = models.BooleanField(default=0)
    comment = models.TextField(blank=True, verbose_name="Комментарий администратора")
    class Meta:
        managed = True
        db_table = 'card'


