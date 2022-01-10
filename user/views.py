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

            if is_realtor=='True':
                is_realtor=True
            else:
                is_realtor=False
            if password==re_password:
                #TODO: validate password
            else:
                return Response(
                    {'error':'Passwords do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except:
            return Response(
                {'error':'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
