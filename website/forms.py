from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.layout import Div
from crispy_forms.layout import Field
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):

	name = forms.CharField(
		required = True,
		widget=forms.TextInput(attrs={'placeholder': _('Name*'),
									  'maxlength': '25',
									}),
		label=''
		)

	email = forms.EmailField(
		required = True,
		widget=forms.TextInput(attrs={'placeholder': _('Email*'),
									  'maxlength': '50',
									}),
		label=''
		)

	message = forms.CharField(
		required = True,
		widget=forms.Textarea(attrs={'placeholder': _('Message*'),
									 'maxlength': '850',
									}),
		label=''
		)