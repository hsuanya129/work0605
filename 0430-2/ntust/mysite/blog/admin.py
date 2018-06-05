
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Category,Cards
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Cards)