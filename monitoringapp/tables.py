import django_tables2 as tables
from .models import *

import itertools


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
                  'status',
                  'reason',
                  'measure',
                  'forecast',
                  'verificator')