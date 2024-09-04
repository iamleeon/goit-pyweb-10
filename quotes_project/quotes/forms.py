from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    born_date = CharField(required=True, widget=TextInput())
    born_location = CharField(required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):

    quote = CharField(min_length=3, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['tags']
