# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serilazers import StudentSerilazer
# from rest_framework import status
# from rest_framework.views import APIView

# from .models import Student
# from.serilazers import StudentSerilazer
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from.models import Student
from.serilazers import StudentSerilazer


class Studentlist(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer


class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class StudentRetriavte(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class StudentCrate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class StudentRu(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer

class Studentde(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerilazer
























# class StudentApiView(GenericAPIView,ListModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerilazer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class StudentApiViewget(GenericAPIView,CreateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerilazer
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    

# class StudentApipost(GenericAPIView,RetrieveModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerilazer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
# class StudentApiUpdate(GenericAPIView,UpdateModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerilazer
#     def get(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
# class StudentApidelete(GenericAPIView,DestroyModelMixin):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerilazer
#     def delete(self,request,*args,**kwargs):
#         return self.delete(request,*args,**kwargs)


# Create your views here.
# class StudentApi(APIView):
#     def get(self,request,pk=None,format=None):
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serilazers=StudentSerilazer(stu)
#             return Response(serilazers.data)
#         stu=Student.objects.all()
#         serilazers=StudentSerilazer(stu)
#         return Response(serilazers.data)
    
#     def post(self,request,format=None):
#          serilazers=StudentSerilazer(data=request.data)
#          if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':'Data Create'},status=status.HTTP_201_CREATED)
#          return Response(serilazers.errors,status=status.HTTP_400_BAD_REQUEST)
#     def put(self,request,pk,format=None):
#          id=pk
#          stu=Student.objects.get(pk=id)
#          serilazers=StudentSerilazer(stu,data=request.data,)
#          if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':' Complete Update create data'})
#          return Response(serilazers.errors)
    

#     def patch(self,request,pk,format=None):
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serilazers=StudentSerilazer(stu,data=request.data, partial=True)
#         if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':'Update create data'})
#         return Response(serilazers.errors)
    

#     def delete(self,request,pk,format=None):
#          id =pk
#          stu=Student.objects.get(pk=id)
#          stu.save()
#          return Response({"msg":"Data deleted"})
# # api view

# @api_view(['GET','POST','PUT','DELETE','PATCH'])
# def student(request,pk=None):
#     if request.method == "GET":
#         id=pk
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serilazers=StudentSerilazer(stu)
#             return Response(serilazers.data)
#         stu=Student.objects.all()
#         serilazers=StudentSerilazer(stu)
#         return Response(serilazers.data)
    
#     if request.method =='POST':
#         serilazers=StudentSerilazer(data=request.data)
#         if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':'Data Create'},status=status.HTTP_201_CREATED)
#         return Response(serilazers.errors,status=status.HTTP_400_BAD_REQUEST)
    

#     if request.method == 'PUT':
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serilazers=StudentSerilazer(stu,data=request.data,)
#         if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':' Complete Update create data'})
#         return Response(serilazers.errors)
    
#     if request.method == 'PTACH':
#         id=pk
#         stu=Student.objects.get(pk=id)
#         serilazers=StudentSerilazer(stu,data=request.data, partial=True)
#         if serilazers.is_valid():
#             serilazers.save()
#             return Response({'msg':'Update create data'})
#         return Response(serilazers.errors)
    
    
#     if request.method == 'DELETE':
#         id =pk
#         stu=Student.objects.get(pk=id)
#         stu.save()
#         return Response({"msg":"Data deleted"})
  
    

    


    
    
