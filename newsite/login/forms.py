from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'})) 

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def save(self,commit=True):
		user = super(signupform,self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()
		return user
		
	# def __init__(self, *args, **kwargs):
	# 	super(RegisterUserForm, self).__init__(*args, **kwargs)

	# 	self.fields['username'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password1'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password2'].widget.attrs['class'] = 'form-control'