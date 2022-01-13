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
    def post(self, request):
        try:
            user = request.user

            if not user.is_realtor:
                return Response(
                    {'error': 'User does not have necessary permissions for creating this listing data'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            data = self.retrieve_values(data)

            if data == -1:
                return Response(
                    {'error': 'Price must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif data == -2:
                return Response(
                    {'error': 'Bedrooms must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif data == -3:
                return Response(
                    {'error': 'Bathrooms must be a floating point value'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            title = data['title']
            slug = data['slug']
            address = data['address']
            city = data['city']
            state = data['state']
            zipcode = data['zipcode']
            description = data['description']
            price = data['price']
            bedrooms = data['bedrooms']
            bathrooms = data['bathrooms']
            sale_type = data['sale_type']
            home_type = data['home_type']
            main_photo = data['main_photo']
            photo_1 = data['photo_1']
            photo_2 = data['photo_2']
            photo_3 = data['photo_3']
            is_published = data['is_published']

            if Listing.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'Listing with this slug already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            Listing.objects.create(
                realtor=user.email,
                title=title,
                slug=slug,
                address=address,
                city=city,
                state=state,
                zipcode=zipcode,
                description=description,
                price=price,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                sale_type=sale_type,
                home_type=home_type,
                main_photo=main_photo,
                photo_1=photo_1,
                photo_2=photo_2,
                photo_3=photo_3,
                is_published=is_published
            )

            return Response(
                {'success': 'Listing created successfully'},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                {'error': 'Something went wrong when creating listing'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )