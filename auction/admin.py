from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Contact

admin.site.register(UserProfile)

class ContactAdmin(admin.ModelAdmin):
    list_display=('c_name','c_email','c_subject','c_message')
admin.site.register(Contact,ContactAdmin)   #modelname,classname
