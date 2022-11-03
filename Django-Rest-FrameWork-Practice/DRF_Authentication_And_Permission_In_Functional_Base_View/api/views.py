from django.shortcuts import render
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH' ,'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk = None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stuData = Student.objects.get(id=id)
            serializers = StudentSerializer(stuData)
            return Response(serializers.data)
        stuData = Student.objects.all()
        serializers = StudentSerializer(stuData,many=True)
        return Response(serializers.data)
    
    if request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data inserted'})
        return Response(serializers.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stuData = Student.objects.get(pk=id)
        serializers = StudentSerializer(stuData,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data Updated'})
        return Response(serializers.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stuData = Student.objects.get(pk=id)
        stuData.delete()
        return Response({'msg':'data Deleted'})



