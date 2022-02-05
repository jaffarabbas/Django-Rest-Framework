import json
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# for single model      
def Student_detail(request, pk):
    stuDetail = Student.objects.get(id = pk)
    serializers = StudentSerializer(stuDetail)
    # json_data = JSONRenderer().render(serializers.data)
    # return HttpResponse(json_data , content_type="application/json")
    return JsonResponse(serializers.data)

# for all data
def Student_List(request):
    stuDetail = Student.objects.all()
    serializers = StudentSerializer(stuDetail, many=True)
    # json_data = JSONRenderer().render(serializers.data)
    # return HttpResponse(json_data , content_type="application/json")
    return JsonResponse(serializers.data, safe=False)
