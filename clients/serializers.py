from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User
from django.utils.timezone import localtime
class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="username")
    class Meta:
        model = User
        fields = ['id', 'name']
    

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    client=serializers.CharField(source='client.client_name',read_only=True)
    created_at = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Project
        fields = ['id', 'project_name','client','users','created_at','created_by']
    
    def get_created_at(self, obj):
        # This will returns: "2019-12-24T11:03:55.931739+05:30"
        return localtime(obj.created_at).astimezone().isoformat()


class GetAllProjects(serializers.ModelSerializer):

  
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    created_at = serializers.SerializerMethodField()
   
    
    class Meta:
        model = Project
        fields = ['id', 'project_name','created_at','created_by']
    

    def get_created_at(self, obj):
        # This will returns: "2019-12-24T11:03:55.931739+05:30"
        return localtime(obj.created_at).astimezone().isoformat()

  

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_name', 'users']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    created_at = serializers.SerializerMethodField()
    

    
    class Meta:
        model = Client
        fields = ['id','client_name','created_at','created_by']

    def get_created_at(self, obj):
        # This will returns: "2019-12-24T11:03:55.931739+05:30"
        return localtime(obj.created_at).astimezone().isoformat()


class ProjectMiniSerializer(serializers.ModelSerializer):
    # Only include "id" and "name" in project response
    name = serializers.CharField(source="project_name")

    class Meta:
        model = Project
        fields = ["id", "name"]

class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    projects= ProjectMiniSerializer(many=True, read_only=True)
    

    class Meta:
        model = Client
        fields = ['id', 'client_name', "projects",'created_at', 'created_by', 'updated_at']
    

    def get_created_at(self, obj):
        # This will returns: "2019-12-24T11:03:55.931739+05:30"
        return localtime(obj.created_at).astimezone().isoformat()

    def get_updated_at(self, obj):
        return localtime(obj.updated_at).astimezone().isoformat()






class ClientPostDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
 
    
  

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
    

    def get_created_at(self, obj):
        # This will returns: "2019-12-24T11:03:55.931739+05:30"
        return localtime(obj.created_at).astimezone().isoformat()

    def get_updated_at(self, obj):
        return localtime(obj.updated_at).astimezone().isoformat()