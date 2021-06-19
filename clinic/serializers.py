from clinic import models
from rest_framework import serializers
from .models import Blog, Career, Comments, Contact, Departments, Professional


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Blog


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Departments

class CareerListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Career

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields ="__all__"
        model = Comments

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Contact

class ProfessionaListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Professional
