from django.contrib import admin
from register.models import Library  

class LipAdmin(admin.ModelAdmin):
    l = ['book_name','book_details']

admin.site.register(Library,LipAdmin)