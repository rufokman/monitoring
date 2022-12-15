from django import forms
from .models import *
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
import re
import numpy as np


class AdminCardsForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = [
            'updated_at',
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
            'status',
            'reason',
            'measure',
            'forecast',
            'verificator',
            'comment',

        ]
        widgets = {
            'updated_at': forms.TextInput(attrs={'readonly':'readonly'}),
            'name_of_user': forms.TextInput(attrs={'readonly': 'readonly'}),
            'organization': forms.TextInput(attrs={'readonly': 'readonly'}),
            'role': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'fio': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'name': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'status': forms.HiddenInput(),
            'verificator': forms.HiddenInput(),
            'type': forms.TextInput(attrs={'readonly': 'readonly'}),
            'method': forms.TextInput(attrs={'readonly': 'readonly'}),
            'low_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'target_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'high_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'weight': forms.TextInput(attrs={'readonly': 'readonly'}),
            'comment': forms.Textarea(attrs={'rows': 2})

        }


AdminCardFormSet = modelformset_factory(
    model=Card,
    form=AdminCardsForm,
    extra=0,
)