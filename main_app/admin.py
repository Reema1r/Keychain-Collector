from django.contrib import admin
from .models import Keychain, KeychainImage, Tag

# Register your models here.
admin.site.register(Keychain)
admin.site.register(KeychainImage)
admin.site.register(Tag)