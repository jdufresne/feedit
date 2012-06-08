from django import forms


class OpmlForm(forms.Form):
    file = forms.FileField(label="OPML file")
