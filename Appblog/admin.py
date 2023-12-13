from django.contrib import admin

from .models import post

admin.site.register(post)

from .models import secondpost

admin.site.register(secondpost)

from .models import tercero

admin.site.register(tercero)

# Register your models here.
