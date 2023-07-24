from django.shortcuts import render
from .forms import contactForm
from django.contrib import messages
# Create your views here.

def index_view(request):
   return render(request, 'website/index.html')

def contect_view(request):
   if request.method == 'POST':
      form = contactForm(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request,messages.SUCCESS,'your ticket submited successfuly')
      else:
         messages.add_message(request, messages.ERROR, 'your ticket didnt submited ')
   form = contactForm()
   return render(request, 'website/contact.html', {'form':form})