from django import forms
# from .models import SignatureUpload

# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = SignatureUpload
#         fields = ['referenceCode', 'firstName', 'lastName', 'emailAddress', 'image']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['referenceCode'].label = 'Reference Code'
#         self.fields['firstName'].label = 'First Name'
#         self.fields['lastName'].label = 'Last Name'
#         self.fields['emailAddress'].label = 'Email Address'
#         self.fields['image'].label = 'Upload Image'