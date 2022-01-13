from os import stat
import rest_framework
from rest_framework import request
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Listing

class ManageListing(APIView):
    def get(self, request, format=None):
        pass
    def post():
        try:
            user=request.user
            if not user.is_realtor:
                return Response(
                    {'error':'User does not have necessary permissions for creating this listing data' },
                    status=status.HTTP_403_FORBIDDEN
                )
            data=request.data

            title = data['title']
            slug = data['slug']
            address = data['address']
            city = data['city']
            state = data['state']
            zipcode = data['zipcode']
            description = data['description']
            price = data['price']
            try:
                price=int(price)
            except:
                return Response(
                    {'error':'Price must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            bedrooms = data['bedrooms']
            bathrooms = data['bathrooms']
            sale_type = data['sale_type']
            home_type = data['home_type']
            main_photo = data['main_photo']
            photo_1 = data['photo_1']
            photo_2 = data['photo_2']
            photo_3 = data['photo_3']
            is_published = data['is_published']


        except:
            return Response(
                {'error':'something went wrong when creating listing'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

