from django.http import HttpResponse
from django.template import loader
from .forms import UploadImageForm
from tempfile import *
from .validate_image import *

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            maybe_image = form.cleaned_data['file_field']
            if valid_image(maybe_image):
                return HttpResponse('Hey, thanks!')
            else:
                return HttpResponse("That's not a valid image!")
        else:
            return HttpResponse("There's something wrong with your form...")
        
    elif request.method == 'GET':
        template = loader.get_template('index.html')
        form = UploadImageForm()
        return HttpResponse(template.render({'form': form}, request))
