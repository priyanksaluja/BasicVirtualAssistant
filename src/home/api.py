from home.models import UserDetails, UserActivities
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterUser(APIView):
    '''
    Service post call request.. This will add user to respective model.
    It will accept models with post method
    '''

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                first_name = serializer.validated_data['first_name']
                last_name = serializer.validated_data['last_name']
                age = serializer.validated_data['age']
                host = serializer.validated_data['host']
                request_type = serializer.validated_data['request_type']
                keywords = serializer.validated_data['keywords']
                if request_type is not 'Wiki Search':
                    UserDetails.objects.create(first_name=first_name, last_name=last_name, age=age)
                UserActivities.objects.create(first_name=first_name, last_name=last_name,
                                              request_type=request_type, terminal=host, keywords=keywords)
                responsecode = status.HTTP_200_OK
                print (first_name, last_name, age, request_type, host, keywords)
            except:
                responsecode = status.HTTP_501_NOT_IMPLEMENTED
        else:
            responsecode = status.HTTP_400_BAD_REQUEST
        return Response(status=responsecode)
