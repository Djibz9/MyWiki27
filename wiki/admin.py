from django.contrib import admin
from .models import UserFileUpload
from .models import Page

admin.site.register(Page)
admin.site.register(UserFileUpload)
# Register your models here.
