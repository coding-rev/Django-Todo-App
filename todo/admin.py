from django.contrib import admin
from .models import TodoModel

# Customizing admin page
admin.site.site_header 		= "Todo List App"
admin.site.site_title 		= "Todo List App"

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
	list_display = ["todo_body", 'finished', 'date_created', 'date_updated']

admin.site.register(TodoModel, TodoAdmin)