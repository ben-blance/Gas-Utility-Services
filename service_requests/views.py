from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServiceRequestForm, TrackingForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save()
            messages.success(
                request,
                f'Your request has been submitted successfully! Your tracking ID is: {service_request.tracking_id}'
            )
            return redirect('request_confirmation', tracking_id=service_request.tracking_id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

def track_request(request):
    form = TrackingForm()
    service_request = None
    
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            try:
                service_request = ServiceRequest.objects.get(tracking_id=tracking_id)
            except ServiceRequest.DoesNotExist:
                messages.error(request, 'Invalid tracking ID. Please try again.')
    
    return render(request, 'service_requests/track_request.html', {
        'form': form,
        'service_request': service_request
    })

def request_confirmation(request, tracking_id):
    try:
        service_request = ServiceRequest.objects.get(tracking_id=tracking_id)
        return render(request, 'service_requests/confirmation.html', {
            'service_request': service_request
        })
    except ServiceRequest.DoesNotExist:
        messages.error(request, 'Invalid tracking ID.')
        return redirect('submit_request')
