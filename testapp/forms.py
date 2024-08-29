from django import forms
from testapp.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['tasktitle','teskdesc']