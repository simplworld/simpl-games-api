from django import forms

from . import models


class UserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = [
            'canvas_id',
            'username',
            'name',
            'first_name',
            'last_name',
            'password',
            'email',
            # 'is_superuser',
            # 'is_staff',
            'is_active',
        ]
