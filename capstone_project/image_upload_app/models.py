from django.db import models

def signature_image_upload_path(instance, filename):
    # Upload path generator function
    return f'signatures/{instance.referenceCode}/{filename}'

class SignatureUpload(models.Model):
    referenceCode = models.CharField(max_length=15, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailAddress = models.CharField(max_length=30)
    signatureStatus = models.CharField(max_length=1, default='N')
    dateCreated = models.DateTimeField(auto_now=True)
    
    # images
    image = models.ImageField(upload_to=signature_image_upload_path, null=True, blank=True)
    
