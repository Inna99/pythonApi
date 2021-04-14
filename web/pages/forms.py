from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Language


class LanguageModelForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

    def clean_complexity(self):
        complexity = self.cleaned_data['complexity']

        # Проверка того, что сложность не выходит за "нижнюю" границу.
        if complexity < 0:
            raise ValidationError(_('Invalid number - complexity too small'))

        # Проверка того, то сложность не выходит за "верхнюю" границу.
        if complexity > 100:
            raise ValidationError(_('Invalid number - complexity too much'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return complexity
