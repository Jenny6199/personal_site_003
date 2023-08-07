from django import forms
from .models import Article


class AddArticleForm(forms.ModelForm):
    """
    This form create new article.
    Based on forms.ModelForm
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'category',
            'author',
            'image',
            'text'
        ]

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
