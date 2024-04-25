from django.shortcuts import render 
from django.http import HttpResponse
from .models import Image
from .tasks import generate_image

# Create your views here.

def generate(request):
    prompts = [
        "A red flying dog",
        "A husky ninja",
        "A footballer kid",
        "A wizard on Mars",
        "Baby Dragon"
    ]
    for prompt in prompts:
        generate_image.delay(prompt)
    return HttpResponse("Images generatation started. Check the console for progress.")
    

