import openpyxl
from django.http import response, HttpResponse
from django.utils.encoding import escape_uri_path

from .models import *

class User_regForm(forms.ModelForm):

    class Meta:
        model = User_reg

        fields=['NSP','password','adressat','action_id','prichina_id','data_vidachi']

        widgets={
            'data_vidachi': forms.DateInput(attrs={'placeholder': 'ДД-ММ-ГГГГ', 'required': 'required','onfocus': "(this.type='date')"}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Используйте спец. знаки'}),
            'adressat':forms.CheckboxSelectMultiple,
        }




    # def __init__(self, *args, **kwargs):
    #     super(User_regForm, self).__init__(*args, **kwargs)
    #     # Here we will redefine our test field.
    #     if self.instance.data_vidachi:
   # def export_to_EXL(self):



