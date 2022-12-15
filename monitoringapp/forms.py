from django import forms
from .models import *
from django.forms import modelformset_factory


class CardsFormCertain(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'send',
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
            'verificator',
            'name_of_user',

        ]
        widgets = {
            'send': forms.CheckboxInput(),
            'organization': forms.TextInput(attrs={'readonly': 'readonly'}),
            'role': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'fio': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'name': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'status': forms.HiddenInput(),
            'name_of_user': forms.HiddenInput(),
            'verificator': forms.HiddenInput(),
            'comment': forms.TextInput(attrs={'readonly': 'readonly'}),

            'type': forms.TextInput(attrs={'readonly': 'readonly'}),
            'method': forms.TextInput(attrs={'readonly': 'readonly'}),
            'low_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'target_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'high_level': forms.TextInput(attrs={'readonly': 'readonly'}),
            'weight': forms.TextInput(attrs={'readonly': 'readonly'}),

        }


CardFormSetCertain = modelformset_factory(
    model=Card,
    form=CardsFormCertain,
    extra=0,
    can_delete=False,
)

