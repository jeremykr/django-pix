from django.http import HttpResponse
from django.template import loader
from .forms import UploadImageForm

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            return HttpResponse('Hey, thanks!')
        else:
            return HttpResponse("That's not a valid image!")
        
    elif request.method == 'GET':
        template = loader.get_template('index.html')
        form = UploadImageForm()
        return HttpResponse(template.render({'form': form}, request))
