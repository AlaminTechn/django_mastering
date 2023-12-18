from rest_framework import serializers
from .models import Blogs


class BlogSerializers(serializers.ModelSerializer):
    model = Blogs
    fields = ['id', 'tittle', 'reference']
