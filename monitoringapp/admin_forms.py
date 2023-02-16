from django import forms
from .models import *
from django.forms import modelformset_factory


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
            'updated_at': forms.DateTimeInput(format='%d.%m.%Y %H:%M:%S', attrs={'rows': 2, 'readonly': 'readonly'}),
            'name_of_user': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'organization': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'role': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'fio': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'name': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'status': forms.HiddenInput(),
            'verificator': forms.Textarea(attrs={'rows': 2}),
            'type': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'method': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'low_level': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'target_level': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'high_level': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'weight': forms.Textarea(attrs={'rows': 2, 'readonly': 'readonly'}),
            'comment': forms.Textarea(attrs={'rows': 2}),
            'first_quarter': forms.Textarea(attrs={'rows': 2}),
            'second_quarter': forms.Textarea(attrs={'rows': 2}),
            'third_quarter': forms.Textarea(attrs={'rows': 2}),
            'fourth_quarter': forms.Textarea(attrs={'rows': 2}),
            'reason': forms.Textarea(attrs={'rows': 2}),
            'measure': forms.Textarea(attrs={'rows': 2}),
            'forecast': forms.Textarea(attrs={'rows': 2}),


        }


AdminCardFormSet = modelformset_factory(
    model=Card,
    form=AdminCardsForm,
    extra=0,
)