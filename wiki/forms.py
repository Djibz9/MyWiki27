from django.forms import ModelForm
from .models import UserFileUpload
from django import forms
'''this is the class that enables the customisation of the upload button and box on the web app'''
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload']
        # widgets={
        #         "upload": forms.ClearableFileInput(
        #             attrs={
        #                 'placeholder':'Choose file...',
        #                 'class':'custom-file-label',
        #                 'type':'file',

        #             }
        #         )
        # }