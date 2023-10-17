from django import forms

class CameraForm(forms.Form):
    btn_capture = forms.CharField(widget=forms.HiddenInput())
