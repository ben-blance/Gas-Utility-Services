from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'customer_name', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type')
    search_fields = ('tracking_id', 'customer_name', 'email')
    readonly_fields = ('tracking_id', 'created_at', 'updated_at')
