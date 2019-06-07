from django.contrib import admin
from .models import UserFileUpload
from .models import Page

#Models are registered here
admin.site.register(Page)
admin.site.register(UserFileUpload)

