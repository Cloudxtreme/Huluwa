from django import forms


class XForm(forms.Form):
    server = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    os = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})
    )
