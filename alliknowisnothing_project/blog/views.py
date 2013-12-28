from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def archive(request):
    
    return HttpResponse('The archive!')
    
def home(request):
    
    template = loader.get_template('blog/index.html')
    context = RequestContext(request, {
                                       })
    
    return HttpResponse(template.render(context))