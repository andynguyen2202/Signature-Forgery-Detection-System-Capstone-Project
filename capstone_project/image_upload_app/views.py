from pymongo import MongoClient
from django.shortcuts import render
import os
import random
import string
from . import runmodel


client = MongoClient()
db = client['AIMLcapstone']
collection = db['uploadSignatures']

def generate_reference_num(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters.upper()) for _ in range(length))

def home(request):
    return render(request, 'home.html', {})

def upload(request):
    referencecode = generate_reference_num()
    if request.method == 'POST':
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        # emailaddress = request.POST['emailaddress']
        # signaturestatus = 'NEW'
        images = request.FILES.getlist('imagedropzone')
        
        # Save images to the media folder
        folder_path = os.path.join('media', 'signatures', 'genuine', referencecode)
        os.makedirs(folder_path, exist_ok=True)
        
        if images:  # Check if the images list is not empty
            for img in images:
                destination = open(os.path.join(folder_path, img.name), 'wb+')
                if img.multiple_chunks():
                    for chunk in img.chunks():
                        destination.write(chunk)
                else:
                    destination.write(img.read())

                destination.close()

        # Save data to MongoDB
        # document = {
        #     'referenceCode': referencecode,
        #     'firstName': firstname,
        #     'lastName': lastname,
        #     'emailAddress': emailaddress,
        #     'signatureStatus': signaturestatus
        # }
        # collection.insert_one(document)
        
        # CALL MODEL HERE TO TRAIN SIGNATURE        
        
        return render(request, 'upload.html', {'referencecode': referencecode})
    
    return render(request, 'upload.html', {'referencecode': referencecode})

def verify(request):
    if request.method == 'POST':
        referencecode = generate_reference_num()
        folder_path = os.path.join('media', 'signatures', 'verify', referencecode)
        
        uploaded_images = request.FILES.getlist('imagedropzone')  # Fetch uploaded images
        
        # Save images to the media folder
        os.makedirs(folder_path, exist_ok=True)
        for img in uploaded_images:
            destination = open(os.path.join(folder_path, img.name), 'wb+')
            if img.multiple_chunks():
                for chunk in img.chunks():
                    destination.write(chunk)
            else:
                destination.write(img.read())
            destination.close()
        
        images = [os.path.join(folder_path, image) for image in os.listdir(folder_path)]
        
        # CALL MODEL HERE TO VERIFY SIGNATURE
        txt = runmodel.run_project(images)
        
        
        return render(request, 'verify.html', {'images': images, 'result_text': txt})
        
    return render(request, 'verify.html')