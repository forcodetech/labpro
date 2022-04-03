from django.shortcuts import render
from django.http import HttpResponse

from .models import lab_task_summary
from .serializers import lab_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .task import sent_mail_user
from rest_framework import status
from django.http import Http404

def test(request):
    return HttpResponse("hi hello")

class lab_views(APIView):
    def get(self,request,format=None):
        all_data = lab_task_summary.objects.all()
        serializer = lab_serializer(all_data,many=True)
        return Response({"data":serializer.data,"status":"success"})
    def post(self,request,format=None):
        serializer = lab_serializer(data = request.data)
        if serializer.is_valid():
            sent_mail_user.delay(serializer.validated_data["email"],serializer.validated_data["name"])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Lab_Detail(APIView):
    def get_object(self, pk):
        try:
            return lab_task_summary.objects.get(pk=pk)
        except lab_task_summary.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = lab_serializer(obj)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = lab_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response({"user data":"deleted","status":status.HTTP_204_NO_CONTENT})      

