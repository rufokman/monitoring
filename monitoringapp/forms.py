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
            'organization': forms.Textarea(attrs={'rows': 4, 'cols':15, 'readonly': 'readonly', }),
            'role': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly', 'cols':20}),
            'fio': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly',  'cols':10}),
            'name': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly', 'cols':20}),
            'status': forms.HiddenInput(),
            'name_of_user': forms.HiddenInput(),
            'verificator': forms.HiddenInput(),
            'comment': forms.Textarea(attrs={'readonly': 'readonly',  'cols':15, 'rows': 4,}),
            'type': forms.Textarea(attrs={'readonly': 'readonly', 'cols':10, 'rows': 4, }),
            'method': forms.Textarea(attrs={'readonly': 'readonly', 'cols':12, 'rows': 4, }),
            'low_level': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly', 'cols': 10, }),
            'target_level': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly', 'cols':10, }),
            'high_level': forms.Textarea(attrs={'readonly': 'readonly',  'cols':10, 'rows':4}),
            'weight': forms.Textarea(attrs={'readonly': 'readonly',  'cols':3, 'rows':4}),
            'reason': forms.Textarea(attrs={'cols':20, 'rows':4}),
            'measure': forms.Textarea(attrs={'cols':20, 'rows':4}),
            'forecast': forms.Textarea(attrs={'cols':20, 'rows':4}),
            'first_quarter': forms.Textarea(attrs={'cols':10, 'rows':4}),
            'second_quarter': forms.Textarea(attrs={'cols':10, 'rows':4}),
            'third_quarter': forms.Textarea(attrs={'cols':10, 'rows':4}),
            'fourth_quarter': forms.Textarea(attrs={'cols':10, 'rows':4}),
        }


CardFormSetCertain = modelformset_factory(
    model=Card,
    form=CardsFormCertain,
    extra=0,
    can_delete=False,
)
