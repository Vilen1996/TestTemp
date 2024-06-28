from django import forms
from .models import CustomUser, Document


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'company_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'partner_name', 'document_content', 'start_date', 'end_date']
