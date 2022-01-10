from os import name
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


class RegisterView():
    permission_classes =(permissions.AllowAny,)
    def post (self,request):
        try:
            data =request.data
            name=data['name']
            email=data['email']
            password=['password']
            re_password=['re_password']
            is_realtor =data['is_realtor']
            
        except:
            return Response(
                {'error':'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
