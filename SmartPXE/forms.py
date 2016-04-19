from django import forms


class XSelect(forms.ChoiceField):
    widget = forms.Select(attrs={'class': 'form-control'})

    def valid_value(self, value):
        return True

    def to_python(self, value):
        if value in self.empty_values:
            return ''
        return int(value)

    def validate(self, value):
        pass


class XForm(forms.Form):
    client = XSelect()
    os = XSelect()
