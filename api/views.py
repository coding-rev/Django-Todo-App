from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Todo
# Create your views here.


class TodoApiView(APIView):
	serializer_class = TodoSerializer

	def get(self, request):
		try:
			todos 			= Todo.objects.all()
			data 			= TodoSerializer(todos, many=True)
			return Response({
				"status":status.HTTP_200_OK,
				"data": data.data
				}, status.HTTP_200_OK)

		except:
			return Response({
				"status":status.HTTP_500_INTERNAL_SERVER_ERROR,
				"message": "Something went wrong"
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	def post(self, request):
		try:
			data = TodoSerializer(data=request.data)
			data.is_valid(raise_exception=False)
			request_data = data.data

			todo 		= Todo.objects.create(body=request_data["body"])

			return Response({
				"status":status.HTTP_201_CREATED,
				"message": "Todo added successfully"
				},status=status.HTTP_201_CREATED)

		except Exception as e:
			return Response({
				"status":status.HTTP_400_BAD_REQUEST,
				"message": str(e)
				},status=status.HTTP_400_BAD_REQUEST)

	
	

class EditTodoView(APIView):
	serializer_class = EditSerializer

	def put(self, request, todo_id):
		try:
			data = EditSerializer(data=request.data)
			data.is_valid(raise_exception=False)
			request_data = data.data

			getTodo 	= Todo.objects.get(id=todo_id)
			if request_data["done"]==True:
				getTodo.done = True
			else:
				getTodo.done= False 
				 
			if request_data["body"]:
				getTodo.body = request_data["body"]
			getTodo.save()
			return Response({
				"status": status.HTTP_200_OK,
				"message":"Todo modification successful"
				}, status=status.HTTP_200_OK)

		except Todo.DoesNotExist:
			return Response({
				"status":status.HTTP_404_NOT_FOUND,
				"message":"Todo not found"
				}, status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			return Response({
				"status":status.HTTP_500_INTERNAL_SERVER_ERROR,
				"message":str(e)
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteTodoView(APIView):
	def delete(self, request, todo_id):
		try:
			getTodo 	= Todo.objects.get(id=todo_id)
			getTodo.delete()
			return Response({
				"status":status.HTTP_200_OK,
				"message":"Todo removed successfully"
				}, status=status.HTTP_200_OK) 
		except Todo.DoesNotExist:
			return Response({
				"status":status.HTTP_404_NOT_FOUND,
				"message":"Todo not found"
				}, status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			return Response({
				"status":status.HTTP_500_INTERNAL_SERVER_ERROR,
				"message":str(e)
				}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
