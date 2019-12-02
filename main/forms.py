from django import forms

class AddRequestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddRequestForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'width: -webkit-fill-available'

    code = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder':'Simple Game Code'}))
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Game Title'}))
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    icon = forms.ImageField(required=False)
    background = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Please Input a color code or color name'}))