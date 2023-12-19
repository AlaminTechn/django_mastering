from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class TodoView(APIView):
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True).data
        return Response({'status': 200, 'data': serializer})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serializer.data, }, status=HTTP_201_CREATED)
        return Response({'status': 400, 'errors': serializer.errors, }, status=HTTP_400_BAD_REQUEST)
