from django import forms


from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='',
				widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
	description = forms.CharField(required=False)
	email = forms.EmailField()
	pricing = forms.DecimalField(initial=20.22)
								
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'pricing'

		]


def clean_title(self):
	title= self.cleaned_data.get("title")
	if not "CFE" in title:
		raise forms.ValidationError("This is not a valid title")
	if not "news" in title:
		raise forms.ValidationError("This is not a valid title")
	return title

def clean_email(self, *args, **kwargs):
	email = self.cleaned_data.get("enail")
	if not email.endwith("edu"):
		raise forms.ValidationError("This is not a valid email")
	return email


class RawProductionForm(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField()
	pricing 	= forms.DecimalField()