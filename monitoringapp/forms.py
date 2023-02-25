from django import forms
from .models import *
from django.forms import modelformset_factory
from datetime import datetime


class CardsFormCertain(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardsFormCertain, self).__init__(*args, **kwargs)
        self.fields['name_of_user'].required = False
        if self.get_initial_for_field(self.fields['status'], 'status') == 0:  # Если КПЭ согласован, то неизменяемый
            for fieldname in self.fields:
                self.fields[fieldname].disabled = True
        if datetime.now().month <= 3:  # В зависимости от текущего квартала закрываем редактирование
            self.fields['first_quarter'].disabled = True
            self.fields['second_quarter'].disabled = True
            self.fields['third_quarter'].disabled = True
        if (datetime.now().month > 3) and (datetime.now().month <= 6):
            self.fields['second_quarter'].disabled = True
            self.fields['third_quarter'].disabled = True
            self.fields['fourth_quarter'].disabled = True
        if (datetime.now().month > 6) and (datetime.now().month <= 9):
            self.fields['first_quarter'].disabled = True
            self.fields['third_quarter'].disabled = True
            self.fields['fourth_quarter'].disabled = True
        if (datetime.now().month > 9) and (datetime.now().month <= 12):
            self.fields['first_quarter'].disabled = True
            self.fields['second_quarter'].disabled = True
            self.fields['fourth_quarter'].disabled = True

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
            'fio': forms.Textarea(attrs={'rows': 4, 'readonly': 'readonly',  'cols':25}),
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
            'weight': forms.Textarea(attrs={'readonly': 'readonly',  'cols':10, 'rows':4}),
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
