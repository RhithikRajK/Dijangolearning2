from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

#def CBView(request):
#    return HttpResponse("function based view")


#class CBView(View):
#    def get(self,request):
#        return HttpResponse("Class Based Views")

class CBView(TemplateView):
    template_name = 'cbv_app/index.html'
    def get_context_data(self, **kwargs):

        #*args stands for arguments
        #**kwargs stands for keyword arguments takes input as dictionary {'key':'value'}
        context = super().get_context_data(**kwargs)
        context['injecthere'] = 'Basic Injection'
        return context
