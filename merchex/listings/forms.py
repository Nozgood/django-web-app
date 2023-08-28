from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

    #def clean_name(self):
#     self.name = self.name.lower()