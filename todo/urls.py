from django.urls import path 
from .import views
app_name = 'todo'

urlpatterns = [
	path('', views.index, name='index'),
	path('update', views.updateTodo, name="update"),
	path('create', views.createTodo, name='create'),
	path('delete', views.deleteTodo, name='delete')
]