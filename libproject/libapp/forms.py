from django.forms import ModelForm,Form
from django import forms
from django.forms import TextInput,PasswordInput,NumberInput,DateInput
from libapp.models import Profile,MyUser,Login,Issue,Return,Libook
from libapp.admin import UserCreationForm,UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


class UpdateProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields = ['fname', 'lname','gender','clss','section','img','dob']
		labels={
					 'fname':'First Name',
					 'lname':'Last Name',
					 'gender':'Gender',
					 'clss':'Class',
					 'section':'Section',
					 'img':'Your Profile Picture',
					 'dob':'Date of Birth',
					 }
		widgets={
	'dob':TextInput(attrs={'type':'date'}),
	}
	
class SignupForm(UserCreationForm):
	class Meta:
		model=MyUser
		fields=['roll','password1','password2']
		widgets = {
		'roll':NumberInput(attrs={'class': 'signup-roll'}),
	'password1':PasswordInput(attrs={'class':'signup-pass'}),
		'password2':PasswordInput(attrs={'class':'signup-pass'}),
		}

		
class LoginForm(AuthenticationForm):
	username = forms.IntegerField(label="Roll Number",widget=forms.NumberInput)

class IssueBookForm(ModelForm):
	class Meta:
		model=Issue
		fields = "__all__"
		exclude = ['issuedate']
		widgets = {
		'roll':NumberInput(attrs={'readonly': 'readonly'}),
		'bid':TextInput(attrs={'readonly': 'readonly'}),
		'bname':TextInput(attrs={'readonly': 'readonly'}),
		}

class SearchBookForm(Form):
	bid = forms.CharField(label="Book Id",widget=forms.TextInput)
	#choice=forms.IntegerField(label="Choice",widget=forms.HiddenInput)

class ReturnBookForm(ModelForm):
	class Meta:
		model=Return
		fields = "__all__"
		exclude = ['returndate']
		widgets = {
		'roll':NumberInput(attrs={'readonly': 'readonly'}),
		'bid':TextInput(attrs={'readonly': 'readonly'}),
		'bname':TextInput(attrs={'readonly': 'readonly'}),
		}