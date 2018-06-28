from django import forms

class getMsg(forms.Form):
	fileChoices = (
		("null", "Choose type of input you want to upload!"),
		("file", "File"),
		("text", "Text"),
	)

	fileType = forms.ChoiceField(choices = fileChoices, label="File type", initial='', widget=forms.Select(attrs={"class":"browser-default"}), required=True)
	message = forms.CharField(label="Message", max_length=500)
	def clean(self):
		cleaned_data = super(getMsg, self).clean()
		return self.cleaned_data

