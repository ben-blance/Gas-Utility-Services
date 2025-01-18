from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'customer_name', 
                 'contact_number', 'email', 'address']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class TrackingForm(forms.Form):
    tracking_id = forms.UUIDField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your tracking ID'
        })
    )
