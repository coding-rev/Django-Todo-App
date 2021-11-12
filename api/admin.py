from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.site_title = "Todo Admin"
admin.site.site_header = "Todo Admin"


admin.site.register(Todo)