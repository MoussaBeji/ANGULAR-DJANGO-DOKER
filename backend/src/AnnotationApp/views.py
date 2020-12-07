from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import random

from AnnotationApp.models import Labels
from AnnotationApp.serializers import LabelSerializer
import json

from django.core.files.storage import default_storage
@csrf_exempt
def labelApi(request,id=0):
    if request.method=='GET':
        labels = Labels.objects.all()
        labels_serializer = LabelSerializer(labels, many=True)
        return JsonResponse(labels_serializer.data, safe=False)

    elif request.method=='POST':
        label_data=JSONParser().parse(request)
        label_serializer = LabelSerializer(data=label_data)
        if label_serializer.is_valid():
            label_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        label_data = JSONParser().parse(request)
        label=Labels.objects.get(LabelId=label_data['LabelId'])
        label_serializer=LabelSerializer(label,data=label_data)
        if label_serializer.is_valid():
            label_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        label=Labels.objects.get(LabelId=id)
        label.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)


@csrf_exempt
def ExportFile(request):
    if request.method== 'POST':
        data=JSONParser().parse(request)
        with open("exported_data.json", "w")as file:
            json.dump(data, file)

        with open("exported_data.json", "rb")as f:
            file_name = default_storage.save(f.name.split('.')[0] +str(random.randint(100,999))+'.json', f)


    return JsonResponse(f"{file_name} succfuly exported",safe=False)
