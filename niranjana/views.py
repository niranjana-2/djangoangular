from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import studentserializer
from .models import Student
from rest_framework.response import Response
# Create your views here.


@api_view(["POST"])
def task_page(request):
    print(request.data)
    serializer1=studentserializer(data=request.data)
    if serializer1.is_valid():
        serializer1.save()
        return Response({"values":serializer1.data})
    return Response("Failed")

@api_view(['GET'])
def task_view(request):
    students= Student.objects.all()
    serializer=studentserializer(students,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def task_update(request,task_id):
      task = Student.objects.get(id=task_id)
      serializer = studentserializer(task, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({"message":"Student updated successfully","data":serializer.data})
      return Response({'errors': serializer.errors}) 


@api_view(['DELETE'])
def task_delete(request,task_id): 
          task = Student.objects.get(id=task_id)
          task.delete()
          return Response({"message":"task deleted successfully"})
