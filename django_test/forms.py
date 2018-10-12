from django import forms

from django_test.models import User


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'city']