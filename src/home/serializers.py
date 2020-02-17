from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    '''
    Serializer to handle input data sent in request
    '''
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    host = serializers.CharField(required=True)
    request_type = serializers.CharField(required=True)
    keywords = serializers.CharField(required=True)