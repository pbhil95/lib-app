from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from libapp.models import MyUser ,Profile

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	class Meta:
		model = MyUser
		fields = ('roll',)
	
	def clean_password2(self): 
		 password1 = self.cleaned_data.get("password1")
		 password2 = self.cleaned_data.get("password2")
		 if password1 and password2 and password1 != password2:
		 	raise forms.ValidationError("Passwords don't match")
		 return password2
	
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()
	class Meta:
		model = MyUser
		fields = ('roll', 'password', 'is_active', 'is_admin')
	
	def clean_password(self):
		 return self.initial["password"]

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	fk_name = 'roll'	 

class UserAdmin(BaseUserAdmin):
	 form = UserChangeForm
	 add_form = UserCreationForm
	 inlines = (ProfileInline, )
	 
	 def get_inline_instances(self, request, obj=None):
	 	if not obj:
	 		return list()
	 	return super(UserAdmin, self).get_inline_instances(request, obj)
		
	 list_display = ('roll','is_admin')
	 list_filter = ('is_admin',)
	 fieldsets = (
	 (None, {'fields': ('roll', 'password')}), ('Permissions', {'fields': ('is_admin',)}),
	 )
	 add_fieldsets = (
	 (None, {
	 			'classes': ('wide',), 'fields': ('roll', 'password1', 'password2'),
	 			}),
	 		)
	 search_fields = ('roll',)
	 ordering = ('roll',)
	 filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)

admin.site.unregister(Group)

