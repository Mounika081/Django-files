from djboot.models import Student
from django.forms import ModelForm
from django import forms

class UsForms(ModelForm):
	class Meta:
		model = Student
		fields = "__all__"
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Name",
			}),
		"rollno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your RollNumber",
			}),
		"branch":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Branch",
			}),
		"year":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Year",
			}),
		}
					


