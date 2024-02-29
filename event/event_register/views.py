from django.shortcuts import render,redirect
from .forms import EventForm
from .models import Event
from .models import *


# Create your views here.
def event_list(request):
   context = {'event_list':Event.objects.all()} 
   return render (request,"event_register/event_list.html",context)

def event_form(request,id=0):
  if request.method == "GET":
   if id==0:
     form=EventForm()
   else:
     event=Event.objects.get(pk=id)
     form=EventForm(instance=event) 
  
   return render (request,"event_register/event_form.html",{'form':form})
  else:
    form =  EventForm(request.POST)
    if form.is_valid():
       form.save()
    return redirect('/event/list')

def event_delete(request):
 return