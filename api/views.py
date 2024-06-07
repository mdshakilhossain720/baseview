from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serilazers import StudentSerilazer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student(request,pk=None):
    if request.method == "GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serilazers=StudentSerilazer(stu)
            return Response(serilazers.data)
        stu=Student.objects.all()
        serilazers=StudentSerilazer(stu)
        return Response(serilazers.data)
    
    if request.method =='POST':
        serilazers=StudentSerilazer(data=request.data)
        if serilazers.is_valid():
            serilazers.save()
            return Response({'msg':'Data Create'},status=status.HTTP_201_CREATED)
        return Response(serilazers.errors,status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        id=pk
        stu=Student.objects.get(pk=id)
        serilazers=StudentSerilazer(stu,data=request.data,)
        if serilazers.is_valid():
            serilazers.save()
            return Response({'msg':' Complete Update create data'})
        return Response(serilazers.errors)
    
    if request.method == 'PTACH':
        id=pk
        stu=Student.objects.get(pk=id)
        serilazers=StudentSerilazer(stu,data=request.data, partial=True)
        if serilazers.is_valid():
            serilazers.save()
            return Response({'msg':'Update create data'})
        return Response(serilazers.errors)
    
    
    if request.method == 'DELETE':
        id =pk
        stu=Student.objects.get(pk=id)
        stu.save()
        return Response({"msg":"Data deleted"})
  
    

    


    
    
