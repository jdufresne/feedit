from django import forms


class NewFeedForm(forms.Form):
    uri = forms.URLField()


class OpmlForm(forms.Form):
    file = forms.FileField(label="OPML file")
