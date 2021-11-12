from django.urls import path
from .import views

app_name = 'api'

urlpatterns = [
	path('retrieve-and-create-todos', views.TodoApiView.as_view(), name="todos-cr"),
	path('edit-todo/<int:todo_id>', views.EditTodoView.as_view(), name="todo-u"),
	path('delete-todo/<int:todo_id>', views.DeleteTodoView.as_view(), name="todo-del")
]