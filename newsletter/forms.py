from django import forms

from .models import SignUp



class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		### exclude = ['full_name']

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		qs = SignUp.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("This email already exists")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name