
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Note
from .serializers import NotenSerializer

@csrf_exempt
def noten_list(request):

    if request.method == 'GET':
        noten = Note.objects.all()
        serializer = NotenSerializer(noten, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = NotenSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        print("hi")
        data = JSONParser().parse(request)
        serializer = NotenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
# Create your views here.
