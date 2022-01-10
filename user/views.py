from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


class RegisterView():
    permission_classes =(permissions.AllowAny,)
    def post (self,request):
        try:
            pass
        except:
            return Response(
                {'error':'Something went wrong when registering an account'},
                
            )
