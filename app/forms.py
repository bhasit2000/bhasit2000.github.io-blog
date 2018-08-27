from django import forms
from django.utils import timezone

class PostForm(forms.Form):

	name = forms.CharField(max_length=30,
		widget=forms.TextInput(attrs={'class': 'input2' , 'name' : 'name' , 'type' : 'text'}))
	title = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs={'class': 'input2' , 'name' : 'title' , 'type' : 'text'}))
	body = forms.CharField(widget=forms.Textarea(attrs={'class':'input2', 'name' : 'post'}))
	
