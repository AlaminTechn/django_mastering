from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blogs
from .serializers import BlogSerializers


# Create your views here.


class BlogView(APIView):

    def get(self, request, *args, **kwargs):
        posts = Blogs.Objects.all()
        serializer = BlogSerializers(posts)

        return Response(serializer.data, )
