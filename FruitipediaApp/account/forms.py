from django import forms

from FruitipediaApp.account.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['image_url', 'age']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': ''
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['email', 'password']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image_url': 'Image URL:',
            'age': 'Age:'
        }
