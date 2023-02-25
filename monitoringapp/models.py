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
    updated_at = models.DateTimeField(verbose_name='Последнее обновление')
    status = models.PositiveIntegerField(choices=status_list, default=3, verbose_name="Статус")
    send = models.BooleanField(default=False, verbose_name="Выбрать все")
    name_of_user = models.TextField(verbose_name='ФИО пользователя')
    organization = models.CharField(verbose_name="Организация", max_length=300)
    role = models.CharField(max_length=1000, verbose_name="Должность")
    fio = models.CharField(max_length=1000, verbose_name="ФИО сотрудника, в чью карту устанавливается КПЭ")
    id_kpi = models.CharField(max_length=300, verbose_name='Идентификатор КПЭ', default='-')
    type = models.CharField(max_length=100, verbose_name='КПЭ/КлС', default='-')
    name = models.CharField(max_length=1000, verbose_name='Наименование КПЭ / КлС')
    method = models.CharField(max_length=1000, verbose_name='Тип КПЭ/КлС')
    low_level = models.CharField(max_length=3000, verbose_name='Нижний уровень')
    target_level = models.CharField(max_length=3000, verbose_name='Целевой уровень')
    high_level = models.CharField(max_length=3000, verbose_name="Верхний уровень")
    weight = models.IntegerField(verbose_name='Вес КПЭ/Значимость КлС')
    first_quarter=models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 1 кв')
    second_quarter=models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 2 кв')
    third_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 3 кв')
    fourth_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 4 кв')
    reason = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Причина отклонения')
    measure = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Мероприятия по снижению риска невыполнения')
    forecast = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Прогнозируемый результат после реализации мероприятий')
    verificator = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Верификатор')
    delete = models.BooleanField(default=0)
    comment = models.TextField(blank=True, verbose_name="Комментарий СУП УК")

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()  # Сохраняем дату изменения формы
        if self.pk is not None:
            orig = Card.objects.get(pk=self.pk)
            if orig.status != self.status:
                CardLog.objects.create(created_at=self.created_at, updated_at=self.updated_at, status=self.status,
                                       send=self.send, name_of_user=self.name_of_user, organization=self.organization,
                                       role=self.role, fio=self.fio, id_kpi=self.id_kpi, type=self.type, name=self.name,
                                       method=self.method, low_level=self.low_level, target_level=self.target_level,
                                       high_level=self.high_level, weight=self.weight, first_quarter=self.first_quarter,
                                       second_quarter=self.second_quarter, third_quarter=self.third_quarter,
                                       fourth_quarter=self.fourth_quarter, reason=self.reason, measure=self.measure,
                                       forecast=self.forecast, verificator=self.verificator, delete=self.delete,
                                       comment=self.comment)
        super(Card, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'card'


class CardLog(models.Model):
    status_list = [(0, 'Согласован'),
                   (1, 'Согласование СУП'),
                   (2, 'На доработке'),
                   (3, 'Новый')]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Последнее обновление')
    status = models.PositiveIntegerField(choices=status_list, default=3, verbose_name="Статус")
    send = models.BooleanField(default=False, verbose_name="Выбрать все")
    name_of_user = models.TextField(verbose_name='ФИО пользователя', blank=True)
    organization = models.CharField(verbose_name="Организация", max_length=300)
    role = models.CharField(max_length=1000, verbose_name="Должность")
    fio = models.CharField(max_length=1000, verbose_name="ФИО сотрудника, в чью карту устанавливается КПЭ")
    id_kpi = models.CharField(max_length=300, verbose_name='Идентификатор КПЭ', default='-')
    type = models.CharField(max_length=100, verbose_name='КПЭ/КлС', default='-')
    name = models.CharField(max_length=1000, verbose_name='Наименование КПЭ / КлС')
    method = models.CharField(max_length=1000, verbose_name='Тип КПЭ/КлС')
    low_level = models.CharField(max_length=3000, verbose_name='Нижний уровень')
    target_level = models.CharField(max_length=3000, verbose_name='Целевой уровень')
    high_level = models.CharField(max_length=3000, verbose_name="Верхний уровень")
    weight = models.IntegerField(verbose_name='Вес КПЭ/Значимость КлС')
    first_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 1 кв')
    second_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 2 кв')
    third_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 3 кв')
    fourth_quarter = models.CharField(max_length=1000, blank=True, verbose_name='Прогноз 4 кв')
    reason = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Причина отклонения')
    measure = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Мероприятия по снижению риска невыполнения')
    forecast = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Прогнозируемый результат после реализации мероприятий')
    verificator = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Верификатор')
    delete = models.BooleanField(default=0)
    comment = models.TextField(blank=True, verbose_name="Комментарий СУП УК")

    class Meta:
        managed = True
        db_table = 'cardlog'

