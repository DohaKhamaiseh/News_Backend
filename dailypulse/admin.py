from django.contrib import admin
from .models import Dailypulse,Reading_later,Comment,News

# Register your models here.
admin.site.register(Reading_later)
admin.site.register(Dailypulse)
admin.site.register(Comment)
admin.site.register(News)
