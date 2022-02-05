from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse

# Create your views here.

def Student_Create(request):
    if(request.method == 'POST'):
        json_data = request.body
        stream =  io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializers = StudentSerializer(data)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':'Data send'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')