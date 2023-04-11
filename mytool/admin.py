from django.contrib import admin
from .models import Tool, Battery

# Register your models here.


# class ToolAdmin(admin.ModelAdmin):
#     fields = ('brand', 'tool_type', 'cordless', 'voltage',
#               'brushless', 'quantity', 'description')


admin.site.register(Tool)
admin.site.register(Battery)
