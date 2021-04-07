from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class AddLanguageForm(forms.Form):
    language = forms.CharField(help_text="Enter name of language.")
    complexity = forms.IntegerField(help_text="Enter a complexity between 0 and 10.")

    def clean_complexity(self):
        data = self.cleaned_data['complexity']

        # Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
        if data < 0:
            raise ValidationError(_('Invalid date - complexity too small'))

        # Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > 10:
            raise ValidationError(_('Invalid date - complexity too much'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data
