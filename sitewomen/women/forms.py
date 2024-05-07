from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from .models import Category, Hasband
from django.core.exceptions import ValidationError
from .models import Women


@deconstructible
class UkrainianValidator:
    ALLOWED_CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяҐАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ0123456789- "
    code = 'ukraine'

    def __init__(self, message=None):
        self.message = message if message else "Повинні бути лише українські літери, дефіс та пробіл"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категорії', empty_label='Категорія не вибрана')
    hasband = forms.ModelChoiceField(queryset=Hasband.objects.all(), label='Чоловік', empty_label='Незаміжня')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'hasband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("довжина перебільшує 50 символів")
        return title

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')
    #file = forms.FileField(label='Файл')