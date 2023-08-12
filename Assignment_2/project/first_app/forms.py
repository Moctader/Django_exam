from django import forms
from first_app.models import To_Do_Model
class To_Do_form(forms.ModelForm):
    class Meta:
        model=To_Do_Model
        fields=[ 'taskTitle', 'taskDescription', 'is_completed']