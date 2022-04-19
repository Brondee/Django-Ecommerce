from django import forms

class SendReview(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label = "", max_length= 800)
