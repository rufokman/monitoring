import django_tables2 as tables
from .models import *

import itertools


class AdminCardTable(tables.Table):
    counter = tables.Column(empty_values=(), orderable=False, verbose_name="№ п/п")
    btnaccept = tables.TemplateColumn(verbose_name=(''),
                                      template_name='btnaccept.html',
                                      orderable=False)

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1

    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ('counter',
                  'updated_at',
                  'status',
                  'name_of_user',
                  'organization',
                  'fio',
                  'role',
                  'type',
                  'name',
                  'method',
                  'low_level',
                  'target_level',
                  'high_level',
                  'weight',
                  'first_quarter',
                  'second_quarter',
                  'third_quarter',
                  'fourth_quarter',
                  'reason',
                  'measure',
                  'forecast',
                  'verificator',
                  'comment',
                  'btnaccept'
                  )


class CardTable(tables.Table):
    counter = tables.Column(empty_values=(), orderable=False, verbose_name="№ п/п")

    def render_counter(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1

    class Meta:
        model = Card
        template_name = "django_tables2/bootstrap.html"
        fields = ('counter',
                  'organization',
                  'fio',
                  'role',
                  'type',
                  'name',
                  'method',
                  'low_level',
                  'target_level',
                  'high_level',
                  'weight',
                  'comment',
                  'first_quarter',
                  'second_quarter',
                  'third_quarter',
                  'fourth_quarter',
                  'reason',
                  'measure',
                  'forecast',
                  'verificator',
                  )