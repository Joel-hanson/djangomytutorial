from django.contrib import admin
from .models import EmployeeEntryData,LeaveModel,ActivateModel
# Register your models here.
admin.site.register(EmployeeEntryData)
admin.site.register(LeaveModel)
admin.site.register(ActivateModel)
