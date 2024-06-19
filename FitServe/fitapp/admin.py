from django.contrib import admin

# Register your models here.
from fitapp.models import Contact, Members


admin.site.register(Contact)
admin.site.register(Members)
