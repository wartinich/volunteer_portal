from django import forms

from assistance.constants import AssistanceStatus
from assistance.models import Assistance, Category


class AssistanceForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.FileField(required=False)
    status = forms.ChoiceField(choices=[(v.name, v.value) for v in AssistanceStatus])

    class Meta:
        model = Assistance
        fields = ["name", "description", "image", "payment_url", "category", "status"]
