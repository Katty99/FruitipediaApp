from django import forms

from FruitipediaApp.fruit.models import Fruit


class FruitFrom(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class EditFruitFrom(FruitFrom):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'image': "Image URL"
        }


class DeleteFruitFrom(FruitFrom):
    class Meta:
        model = Fruit
        fields = '__all__'
        exclude = ['nutrition']
        labels = {
            'name': "Name:",
            'image': "Image URL:",
            'description': "Description:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
