from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model= Event
        #fields='__all__'
        fields=('event_name','date_and_time','location','description','organizer_details')
        labels={
            'event_name':'Event-Title',
            'organizer_details':'email_address'
        }
        
       # def __init__(self,*args,**kwargs):
        #   super (EventForm,self).__init__(*args,**kwargs)
       #self.fields['location'].empty_label="enter_a_place_name"
       
       #self.fields['Event_Title'].required=False

